"""This module provides the ImageTablePanelWidget class."""

import os

from itk import imread
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QHeaderView,
    QInputDialog,
    QStyle,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
)

from .sovImageTableSettings import ImageTableSettings
from .sovImportExportPanelWidget import ImportExportPanelWidget
from .sovUtils import time_and_log
from .ui_sovImageTablePanelWidget import Ui_ImageTablePanelWidget


class ImageTablePanelWidget(QWidget, Ui_ImageTablePanelWidget):
    @time_and_log
    def __init__(self, gui, state, parent=None):
        """Initialize the GUI and state for the application.

        Args:
            gui: The graphical user interface object.
            state: The state object for the application.
            parent: The parent widget (default is None).
        """

        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.settings = ImageTableSettings()

        self.selected = []
        pixmapi = getattr(QStyle, 'SP_DialogApplyButton')
        self.selected_icon = self.style().standardIcon(pixmapi)

        self.imageTableWidget.setRowCount(0)
        self.imageTableWidget.setColumnCount(8)
        self.imageTableWidget.setHorizontalHeaderLabels(
            [
                'Selected',
                'Loaded',
                'Type',
                'Thumbnail',
                'Label',
                'Size',
                'Spacing',
                'Filename',
            ]
        )
        self.col_filetype = 2
        self.col_label = 4
        self.col_filename = 7
        self.imageTableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.imageTableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.imageTableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.imageTableWidget.setShowGrid(True)
        self.imageTableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents
        )
        self.imageTableWidget.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents
        )
        self.imageTableWidget.setIconSize(QSize(75, 75))
        self.imageTableWidget.verticalHeader().hide()
        self.imageTableWidget.setStyleSheet(
            'QTableView{ selection-background-color: rgba(0, 50, 0, 50);  }'
        )

        self.imageTableWidget.cellClicked.connect(self.select_data_by_table)

        self.imageTableLoadButton.clicked.connect(self.load_selected)
        self.imageTableUnloadButton.clicked.connect(self.unload_selected)
        self.imageTableRelabelButton.clicked.connect(self.relabel_selected)
        self.imageTableRemoveButton.clicked.connect(self.remove_selected)
        self.imageTableImportExportButton.clicked.connect(
            self.add_import_export_panel
        )
        self.imageTableExpandButton.clicked.connect(self.expand_table)

        self.enlarged_table = None

        self.fill_table()

    @time_and_log
    def add_import_export_panel(self):
        """Add an image processing panel to the GUI if it does not already exist.

        If the image processing panel does not exist, it creates a new ImageProcessPanelWidget and adds it to the tab widget.
        If the image processing panel already exists, it sets the current widget to the existing panel.

        Args:
            self (object): The current instance of the class.
        """
        if self.gui.importExportPanel is None:
            self.gui.importExportPanel = ImportExportPanelWidget(
                self.gui, self.state
            )
        if self.gui.tabWidget.indexOf(self.gui.importExportPanel) == -1:
            indx = self.gui.tabWidget.indexOf(self.gui.newTaskTab)
            self.gui.tabWidget.insertTab(
                indx, self.gui.importExportPanel, 'Import/Save/Export'
            )
            self.gui.tabWidget.setCurrentWidget(self.gui.importExportPanel)

    @time_and_log
    def unload_selected(self):
        self.selected.sort(reverse=True)
        for row in self.selected:
            if row < len(self.state.image_filename):
                self.gui.unload_image(row, False)
            elif row == len(self.state.image_filename):
                self.gui.unload_scene(False)
        if len(self.selected) > 0:
            self.selected = []
        self.fill_table()

    @time_and_log
    def remove_selected(self):
        self.selected.sort(reverse=True)
        for row in self.selected:
            if row < len(self.state.image_filename):
                fname = self.state.image_filename[row]
                self.gui.unload_image(row, False)
                self.settings.remove_data(fname)
            elif (
                row == len(self.state.image_filename)
                and self.state.scene_filename
                == self.imageTableWidget.item(row, self.col_filename).text()
            ):
                fname = self.state.scene_filename
                self.gui.unload_scene()
                self.settings.remove_data(fname)
            else:
                self.settings.remove_data(
                    self.imageTableWidget.item(row, self.col_filename).text()
                )
        if len(self.selected) > 0:
            self.selected = []
        self.fill_table()

    @time_and_log
    def close_expanded_table(self):
        self.enlarged_table.close()
        self.enlarged_table = None

    @time_and_log
    def expand_table(self):
        if self.enlarged_table is None:
            self.enlarged_table = ImageTablePanelWidget(self.gui, self.state)
            self.enlarged_table.setWindowTitle('Image Table')
            self.enlarged_table.imageTableExpandButton.setText('CLOSE')
            self.enlarged_table.imageTableExpandButton.setMinimumWidth(75)
            self.enlarged_table.imageTableExpandButton.clicked.disconnect()
            self.enlarged_table.imageTableExpandButton.clicked.connect(
                self.close_expanded_table
            )
            self.enlarged_table.show()
        else:
            self.enlarged_table.show()

    @time_and_log
    def update_image(self):
        self.selected = []
        self.fill_table()
        # Probably need to disable selection callback when calling this function
        self.imageTableWidget.selectRow(self.state.current_image_num)

    @time_and_log
    def update_scene(self):
        self.selected = []
        self.fill_table()
        # Probably need to disable selection callback when calling this function
        self.imageTableWidget.selectRow(self.state.current_image_num)

    @time_and_log
    def redraw_image_row(self, row_num):
        """Redraws the image at the specified index in the image table widget.

        This function updates the information displayed in the image table
        widget for the image at the specified index.

        Args:
            self: The object instance.
            img_num (int): The index of the image to be redrawn.


        Raises:
            IndexError: If the specified img_num is out of range.
        """

        img_num = row_num
        col_num = 0
        if row_num in self.selected:
            self.imageTableWidget.setItem(
                row_num, col_num, QTableWidgetItem(self.selected_icon, '')
            )
        else:
            self.imageTableWidget.setItem(
                row_num, col_num, QTableWidgetItem('')
            )
        col_num += 1
        if img_num < len(self.state.image_filename):
            self.imageTableWidget.setItem(
                row_num, col_num, QTableWidgetItem(self.selected_icon, '')
            )
        else:
            print('ERROR: Can only redraw rows for images that are loaded.')
            self.imageTableWidget.setItem(
                row_num, col_num, QTableWidgetItem('')
            )
        col_num += 1
        self.imageTableWidget.setItem(
            row_num, col_num, QTableWidgetItem(str('Image'))
        )
        col_num += 1
        self.imageTableWidget.setItem(
            row_num,
            col_num,
            QTableWidgetItem(QIcon(self.state.image_thumbnail[img_num]), ''),
        )
        col_num += 1
        self.imageTableWidget.setItem(
            row_num,
            col_num,
            QTableWidgetItem(str(self.state.image_label[img_num])),
        )
        col_num += 1
        size_str = [
            str(i)
            for i in self.state.image[img_num]
            .GetLargestPossibleRegion()
            .GetSize()
        ]
        self.imageTableWidget.setItem(
            row_num, col_num, QTableWidgetItem('x'.join(size_str))
        )
        col_num += 1
        spacing_str = [
            f'{i:.4f}' for i in self.state.image[img_num].GetSpacing()
        ]
        self.imageTableWidget.setItem(
            row_num, col_num, QTableWidgetItem(', '.join(spacing_str))
        )
        col_num += 1
        filename = self.state.image_filename[img_num]
        self.imageTableWidget.setItem(
            row_num, col_num, QTableWidgetItem(filename)
        )

    @time_and_log
    def redraw_scene_row(self, row_num):
        col_num = 0
        if row_num in self.selected:
            self.imageTableWidget.setItem(
                row_num, col_num, QTableWidgetItem(self.selected_icon, '')
            )
        else:
            self.imageTableWidget.setItem(
                row_num, col_num, QTableWidgetItem('')
            )
        col_num += 1
        self.imageTableWidget.setItem(
            row_num, col_num, QTableWidgetItem(self.selected_icon, '')
        )
        col_num += 1
        self.imageTableWidget.setItem(
            row_num, col_num, QTableWidgetItem(str('Scene'))
        )
        col_num += 1
        self.imageTableWidget.setItem(
            row_num,
            col_num,
            QTableWidgetItem(QIcon(self.state.scene_thumbnail), ''),
        )
        col_num += 1
        self.imageTableWidget.setItem(
            row_num, col_num, QTableWidgetItem(self.state.scene_label)
        )
        col_num += 1
        size = self.state.scene.GetNumberOfChildren()
        self.imageTableWidget.setItem(
            row_num, col_num, QTableWidgetItem(str(size))
        )
        col_num += 1
        self.imageTableWidget.setItem(
            row_num, col_num, QTableWidgetItem(str('N/A'))
        )
        col_num += 1
        self.imageTableWidget.setItem(
            row_num, col_num, QTableWidgetItem(str(self.state.scene_filename))
        )

    @time_and_log
    def fill_table(self):
        """Fill the image table with images from the state and from settings.

        This method clears the existing image table and fills it with image
        records from the state. It then retrieves file records from the
        settings and adds them to the table if they are not already present.
        For each file record, it populates the table with the file's thumbnail,
        filename, size, and spacing.

        Args:
            self: The instance of the class.
        """

        self.imageTableWidget.clear()
        self.imageTableWidget.setRowCount(0)
        self.imageTableWidget.setHorizontalHeaderLabels(
            [
                'Selected',
                'Loaded',
                'Type',
                'Thumbnail',
                'Label',
                'Size',
                'Spacing',
                'Filename',
            ]
        )
        row_num = 0
        for _ in range(len(self.state.image)):
            self.imageTableWidget.insertRow(row_num)
            self.redraw_image_row(row_num)
            row_num += 1
        if self.state.scene.GetNumberOfChildren() > 0:
            self.imageTableWidget.insertRow(row_num)
            self.redraw_scene_row(row_num)
            row_num += 1

        self.settings.read_file_records()
        for file in self.settings.file_records:
            if (
                file.filename not in self.state.image_filename
                and file.file_type == 'image'
            ):
                self.imageTableWidget.insertRow(row_num)
                col_num = 0
                if row_num in self.selected:
                    self.imageTableWidget.setItem(
                        row_num,
                        col_num,
                        QTableWidgetItem(self.selected_icon, ''),
                    )
                else:
                    self.imageTableWidget.setItem(
                        row_num, col_num, QTableWidgetItem('')
                    )
                col_num += 1
                loaded_text = ' '
                self.imageTableWidget.setItem(
                    row_num, col_num, QTableWidgetItem(loaded_text)
                )
                col_num += 1
                self.imageTableWidget.setItem(
                    row_num, col_num, QTableWidgetItem('Image')
                )
                col_num += 1
                if file.file_thumbnail != '':
                    qthumb = QPixmap(file.file_thumbnail)
                    self.imageTableWidget.setItem(
                        row_num, col_num, QTableWidgetItem(QIcon(qthumb), '')
                    )
                else:
                    self.imageTableWidget.setItem(
                        row_num, col_num, QTableWidgetItem(' ')
                    )
                col_num += 1
                self.imageTableWidget.setItem(
                    row_num, col_num, QTableWidgetItem(str(file.file_label))
                )
                col_num += 1
                self.imageTableWidget.setItem(
                    row_num, col_num, QTableWidgetItem(str(file.file_size))
                )
                col_num += 1
                self.imageTableWidget.setItem(
                    row_num, col_num, QTableWidgetItem(str(file.file_spacing))
                )
                col_num += 1
                self.imageTableWidget.setItem(
                    row_num, col_num, QTableWidgetItem(str(file.filename))
                )
                row_num += 1
            elif (
                file.filename != self.state.scene_filename
                and file.file_type == 'scene'
            ):
                self.imageTableWidget.insertRow(row_num)
                col_num = 0
                if row_num in self.selected:
                    self.imageTableWidget.setItem(
                        row_num,
                        col_num,
                        QTableWidgetItem(self.selected_icon, ''),
                    )
                else:
                    self.imageTableWidget.setItem(
                        row_num, col_num, QTableWidgetItem('')
                    )
                col_num += 1
                loaded_text = ' '
                self.imageTableWidget.setItem(
                    row_num, col_num, QTableWidgetItem(loaded_text)
                )
                col_num += 1
                self.imageTableWidget.setItem(
                    row_num, col_num, QTableWidgetItem('Scene')
                )
                col_num += 1
                qthumb = QPixmap(file.file_thumbnail)
                self.imageTableWidget.setItem(
                    row_num, col_num, QTableWidgetItem(QIcon(qthumb), '')
                )
                col_num += 1
                self.imageTableWidget.setItem(
                    row_num, col_num, QTableWidgetItem(file.file_label)
                )
                col_num += 1
                self.imageTableWidget.setItem(
                    row_num, col_num, QTableWidgetItem(file.file_size)
                )
                col_num += 1
                self.imageTableWidget.setItem(
                    row_num, col_num, QTableWidgetItem('N/A')
                )
                col_num += 1
                self.imageTableWidget.setItem(
                    row_num, col_num, QTableWidgetItem(file.filename)
                )
                row_num += 1

    @time_and_log
    def create_new_image(self):
        self.state.image_label.append(
            os.path.basename(self.state.image_filename[-1])
        )
        self.state.image_thumbnail.append(
            self.settings.get_thumbnail(
                self.state.image[-1], self.state.image_filename[-1], 'image'
            )
        )
        self.settings.add_data(
            self.state.image[-1],
            self.state.image_filename[-1],
            'image',
            self.state.image_label[-1],
            self.state.image_thumbnail[-1],
        )
        self.selected = []
        self.fill_table()

    @time_and_log
    def save_image(self, filename):
        self.settings.add_data(
            self.state.image[self.state.current_image_num],
            filename,
            'image',
            self.state.image_label[self.state.current_image_num],
            self.state.image_thumbnail[self.state.current_image_num],
        )
        self.selected = []
        self.fill_table()

    @time_and_log
    def load_scene(self):
        self.state.scene_thumbnail = self.settings.get_thumbnail(
            self.gui.view3DPanel.get_screenshot(),
            self.state.scene_filename,
            'scene',
        )
        self.state.scene_label = os.path.basename(self.state.scene_filename)
        self.settings.add_data(
            self.state.scene,
            self.state.scene_filename,
            'scene',
            self.state.scene_label,
            self.state.scene_thumbnail,
        )
        self.selected = []
        self.fill_table()

    @time_and_log
    def save_scene(self, filename):
        self.state.scene_thumbnail = self.settings.get_thumbnail(
            self.gui.view3DPanel.get_screenshot(), filename, 'scene', True
        )
        self.state.scene_label = os.path.basename(filename)
        self.settings.add_data(
            self.state.scene,
            filename,
            'scene',
            self.state.scene_label,
            self.state.scene_thumbnail,
        )
        self.fill_table()

    @time_and_log
    def replace_image(self, img_num):
        self.redraw_image_row(img_num)

    @time_and_log
    def relabel_selected(self):
        for row in self.selected:
            widget = QWidget()
            text, ok = QInputDialog.getText(
                widget,
                f'Relabel {self.imageTableWidget.item(row, self.col_label).text()}',
                'New label:',
            )
            if ok:
                self.settings.relabel(
                    self.imageTableWidget.item(row, self.col_filename).text(),
                    text,
                )
                self.imageTableWidget.setItem(
                    row, self.col_label, QTableWidgetItem(text)
                )

    @time_and_log
    def select_data_by_table(self, row, col):
        if col == 0:
            if row in self.selected:
                self.selected.remove(row)
            else:
                self.selected.append(row)
            self.fill_table()
            return
        if row < len(self.state.image_filename):
            self.state.current_image_num = row
            self.gui.update_image()
            if self.state.view2D_overlay_auto_update:
                self.gui.update_overlay()

    @time_and_log
    def load_selected(self):
        for row in self.selected:
            if row >= len(self.state.image_filename):
                if (
                    self.imageTableWidget.item(row, self.col_filetype).text()
                    == 'Image'
                ):
                    self.gui.load_image(
                        self.imageTableWidget.item(
                            row, self.col_filename
                        ).text()
                    )
                elif (
                    self.imageTableWidget.item(row, self.col_filetype).text()
                    == 'Scene'
                ):
                    self.gui.load_scene(
                        self.imageTableWidget.item(
                            row, self.col_filename
                        ).text()
                    )
        self.selected = []
        self.fill_table()

    @time_and_log
    def register_images(self, dir, redraw_table=True):
        files = [
            os.path.join(dir, f)
            for f in os.listdir(dir)
            if os.path.isfile(os.path.join(dir, f))
        ]
        dicom_dir = False
        for filename in files:
            if filename.lower().endswith('.dcm') or filename.endswith(''):
                if dicom_dir:
                    continue
                else:
                    print(f"Adding DICOM object '{filename}' to settings")
                    filename = dir
                    dicom_dir = True
            else:
                print(f"Adding NON-DICOM image '{filename}' to settings")
            try:
                img = imread(filename)
            except Exception:
                continue
            label = os.path.basename(filename)
            thumbnail = self.settings.get_thumbnail(img, filename, 'image')
            self.settings.add_data(
                img,
                filename,
                'image',
                label,
                thumbnail,
            )

        dirs = [
            os.path.join(dir, d)
            for d in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, d))
        ]
        for dirname in dirs:
            self.register_images(dirname, False)

        if redraw_table:
            self.selected = []
            self.fill_table()
