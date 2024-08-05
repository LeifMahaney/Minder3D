from PySide6.QtWidgets import QWidget

from .sovImportDICOMPanelWidget import ImportDICOMPanelWidget
from .sovUtils import time_and_log
from .ui_sovImportExportPanelWidget import Ui_ImportExportPanelWidget


class ImportExportPanelWidget(QWidget, Ui_ImportExportPanelWidget):
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

        self.importExportLoadImageButton.pressed.connect(self.gui.load_image)
        self.importExportLoadImageButton.setStyleSheet(
            'background-color: #00aa00'
        )
        self.importExportLoadOverlayButton.pressed.connect(
            self.gui.load_overlay
        )
        self.importExportLoadSceneButton.pressed.connect(self.gui.load_scene)
        self.importExportImportDICOMButton.pressed.connect(
            self.add_import_DICOM_panel
        )
        self.importExportSaveImageButton.pressed.connect(self.gui.save_image)
        self.importExportSaveOverlayButton.pressed.connect(
            self.gui.save_overlay
        )
        self.importExportSaveVTKModelsButton.pressed.connect(
            self.gui.save_vtk_models
        )
        self.importExportSaveSceneButton.pressed.connect(self.gui.save_scene)

    @time_and_log
    def add_import_DICOM_panel(self):
        """Add the Import DICOM panel to the GUI tab widget if necessary.

        If the Import DICOM panel is not already created, it creates a new
        instance of ImportDICOMPanelWidget and adds it to the tab widget.
        If the Import DICOM panel is already added, it sets the current widget
        to the Import DICOM panel.

        Args:
            self (object): The instance of the class.
        """

        if self.gui.importDICOMPanel is None:
            self.gui.importDICOMPanel = ImportDICOMPanelWidget(
                self.gui, self.state
            )
        if self.gui.tabWidget.indexOf(self.gui.importDICOMPanel) == -1:
            indx = self.gui.tabWidget.indexOf(self.gui.newTaskTab)
            self.gui.tabWidget.insertTab(
                indx, self.gui.importDICOMPanel, 'Import DICOM'
            )
            self.gui.tabWidget.setCurrentWidget(self.gui.importDICOMPanel)
