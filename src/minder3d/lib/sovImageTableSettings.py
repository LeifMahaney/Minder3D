import os
import uuid

import itk
import numpy as np
from PySide6.QtCore import QSettings, QStandardPaths, Qt
from PySide6.QtGui import QImage, QPixmap
from vtk.util.numpy_support import vtk_to_numpy

from .sovUtils import time_and_log


class ImageTableSettingsFileRecord:
    def __init__(
        self,
        filename,
        file_type,
        file_spacing='',
        file_size='',
        file_thumbnail='',
        file_label='',
    ):
        """Initialize the object with the provided file details.

        Args:
            filename (str): The name of the file.
            file_type (str): The type of the file.
            file_spacing (str): A list of spacing details. Defaults to ''.
            file_size (str): A list of size details. Defaults to ''.
            file_thumbnail (str): The thumbnail of the file. Defaults to ''.
            file_label (str): The short diaplay-name of the file. Defaults to ''.
        """

        self.filename = filename
        self.file_type = file_type
        self.file_spacing = file_spacing
        self.file_size = file_size
        self.file_thumbnail = file_thumbnail
        self.file_label = file_label


class ImageTableSettings(QSettings):
    def __init__(self):
        settings_file = os.path.join(
            QStandardPaths.writableLocation(QStandardPaths.AppDataLocation),
            'settings_imagetable.ini',
        )
        os.makedirs(os.path.dirname(settings_file), exist_ok=True)
        super().__init__(settings_file, QSettings.IniFormat)

        self.read_file_records()

    @time_and_log
    def clear_data(self):
        self.clear()
        self.sync()

    @time_and_log
    def read_file_records(self):
        """Get file records from the settings.

        This function retrieves file records from the settings and returns a list of file records.

        Returns:
            list: A list of file records retrieved from the settings.
        """

        self.file_records = []
        size = self.beginReadArray('files')
        for i in range(size):
            self.setArrayIndex(i)
            filename = self.value('filename', '')
            if os.path.exists(filename):
                file_type = self.value('file_type', '')
                file_spacing = self.value('file_spacing', '')
                file_size = self.value('file_size', '')
                file_thumbnail = self.value('file_thumbnail', '')
                file_label = self.value('file_label', '')
                file = ImageTableSettingsFileRecord(
                    filename,
                    file_type,
                    file_spacing,
                    file_size,
                    file_thumbnail,
                    file_label,
                )
                self.file_records.append(file)
        self.endArray()

    @time_and_log
    def write_file_records(self):
        self.clear()
        if len(self.file_records) > 0:
            self.beginWriteArray('files')
            for i, file in enumerate(self.file_records):
                self.setArrayIndex(i)
                self.setValue('filename', file.filename)
                self.setValue('file_type', file.file_type)
                self.setValue('file_spacing', file.file_spacing)
                self.setValue('file_size', file.file_size)
                self.setValue('file_thumbnail', file.file_thumbnail)
                self.setValue('file_label', file.file_label)
            self.endArray()
        self.sync()

    @time_and_log
    def write_thumbnail(self, thumbnail_pixmap):
        if thumbnail_pixmap is not None:
            data_dir = QStandardPaths.writableLocation(
                QStandardPaths.AppDataLocation
            )
            file_thumbnail = str(uuid.uuid4()) + '.png'
            file_thumbnail = os.path.join(data_dir, file_thumbnail)
            if not thumbnail_pixmap.save(file_thumbnail):
                file_thumbnail = ''
            return file_thumbnail

    @time_and_log
    def add_data(
        self, obj, filename, file_type, file_label=None, thumbnail_pixmap=None
    ):
        """Add a file to the settings.

        This function adds a file to the settings, including its filename, type,
        spacing, size, and thumbnail.

        Args:
            obj: The object representing the file.
            filename (str): The name of the file.
            file_type (str): The type of the file.
            file_label (Optional[str]): The custom label of file, defaults to basename of filename
            thumbnail_pixmap (Optional[QPixmap]): The thumbnail of the file.


        Raises:
            IndexError: If the input list is empty.
        """
        filename = os.path.abspath(filename)
        file_spacing = ''
        file_size = ''
        file_thumbnail = ''
        if file_type == 'image':
            file_spacing = ', '.join(
                [str(f'{s:.4f}') for s in obj.GetSpacing()]
            )
            file_size = 'x'.join(
                [str(s) for s in obj.GetLargestPossibleRegion().GetSize()]
            )
        elif file_type == 'scene':
            file_size = str(obj.GetNumberOfChildren())
        if file_label is None or file_label == '':
            file_label = os.path.basename(filename)
        file_thumbnail = self.write_thumbnail(thumbnail_pixmap)

        for i, file in enumerate(self.file_records):
            if file.filename == filename:
                self.file_records[i].file_type = file_type
                self.file_records[i].file_spacing = file_spacing
                self.file_records[i].file_size = file_size
                if self.file_records[i].file_thumbnail != '' and os.path.exists(
                    self.file_records[i].file_thumbnail
                ):
                    os.remove(self.file_records[i].file_thumbnail)
                self.file_records[i].file_thumbnail = file_thumbnail
                self.file_records[i].file_label = file_label
                self.write_file_records()
                return

        if len(self.file_records) > 10:
            if self.file_records[-1].file_thumbnail != '' and os.path.exists(
                self.file_records[-1].file_thumbnail
            ):
                os.remove(self.file_records[-1].file_thumbnail)
            self.file_records.pop(-1)

        file = ImageTableSettingsFileRecord(
            filename,
            file_type,
            file_spacing,
            file_size,
            file_thumbnail,
            file_label,
        )
        self.file_records.append(file)

        self.write_file_records()

    @time_and_log
    def remove_data(self, filename):
        """Remove a file from the settings.

        This function removes a file from the settings.

        Args:
            filename: The name of the file to be removed from settings.

        Raises:
            IndexError: If the input list is empty.
        """
        for i, file in enumerate(self.file_records):
            if file.filename == filename:
                if file.file_thumbnail != '' and os.path.exists(
                    file.file_thumbnail
                ):
                    os.remove(file.file_thumbnail)
                self.file_records.pop(i)
                self.write_file_records()
                return

    @time_and_log
    def relabel(self, filename, new_label):
        filename = os.path.abspath(filename)

        for i, file in enumerate(self.file_records):
            if file.filename == filename:
                self.file_records[i].file_label = new_label
                self.write_file_records()
                return

    @time_and_log
    def get_thumbnail(
        self, obj, filename, file_type, force_new_thumbnail=False
    ):
        """Get the thumbnail of a file.

        This function retrieves the thumbnail of a file from the settings.
        """
        if not force_new_thumbnail:
            for file in self.file_records:
                if file.filename == filename:
                    return QPixmap(file.file_thumbnail)

        if file_type == 'image':
            return self.get_thumbnail_pixmap_from_image(obj)
        elif file_type == 'scene':
            return self.get_thumbnail_pixmap_from_vtk_image(obj)

    @time_and_log
    def get_thumbnail_pixmap_from_image(self, img):
        """Get a thumbnail pixmap from an image."""
        arr = itk.GetArrayFromImage(img)
        flipX = int(np.sign(np.sum(img.GetDirection(), axis=1)[0]))
        flipY = int(np.sign(np.sum(img.GetDirection(), axis=1)[1]))
        thumb_array = arr[arr.shape[0] // 2, ::flipY, ::flipX]
        if len(thumb_array.shape) == 3:
            thumb_array = thumb_array.mean(axis=2).astype(np.uint8)
        auto_range = np.quantile(thumb_array, [0.05, 0.95])
        thumb_array = np.clip(thumb_array, auto_range[0], auto_range[1])
        thumb_array = (
            (thumb_array - auto_range[0])
            / (auto_range[1] - auto_range[0])
            * 255
        ).astype(np.uint8)
        thumb_image = QImage(
            thumb_array.data,
            thumb_array.shape[1],
            thumb_array.shape[0],
            thumb_array.strides[0],
            QImage.Format_Grayscale8,
        )
        thumb_image.setDotsPerMeterX(10 / img.GetSpacing()[0])
        thumb_image.setDotsPerMeterY(10 / img.GetSpacing()[1])
        thumb_pixmap = QPixmap.fromImage(thumb_image).scaled(
            100, 100, Qt.KeepAspectRatio
        )
        return thumb_pixmap

    @time_and_log
    def get_thumbnail_pixmap_from_vtk_image(self, img):
        vtk_array = img.GetPointData().GetScalars()
        np_array = vtk_to_numpy(vtk_array)
        dims = img.GetDimensions()
        np_array = np_array.reshape(dims[1], dims[0], dims[2], -1)

        # Process the NumPy array
        if np_array.shape[3] == 1:
            np_array = np_array[:, :, :, 0]
            np_array = np.stack([np_array] * 3, axis=-1)
        elif np_array.shape[3] == 4:
            np_array = np_array[:, :, :, :3]

        auto_range = np.quantile(np_array, [0.05, 0.95])
        np_array = np.clip(np_array, auto_range[0], auto_range[1])
        np_array = (
            (np_array - auto_range[0]) / (auto_range[1] - auto_range[0]) * 255
        ).astype(np.uint8)

        # Create QImage
        thumb_image = QImage(
            np_array.data,
            np_array.shape[1],
            np_array.shape[0],
            np_array.strides[0],
            QImage.Format_RGB888,
        )
        thumb_image.setDotsPerMeterX(10 / img.GetSpacing()[0])
        thumb_image.setDotsPerMeterY(10 / img.GetSpacing()[1])

        # Convert QImage to QPixmap
        thumb_pixmap = QPixmap.fromImage(thumb_image).scaled(
            100, 100, Qt.KeepAspectRatio
        )
        return thumb_pixmap
