import os

from PySide6.QtCore import QSettings, QStandardPaths

from .sovUtils import time_and_log


class ImportDICOMSettings(QSettings):
    def __init__(self):
        settings_file = os.path.join(
            QStandardPaths.writableLocation(QStandardPaths.AppDataLocation),
            'settings_importdicom.ini',
        )
        os.makedirs(os.path.dirname(settings_file), exist_ok=True)
        super().__init__(settings_file, QSettings.IniFormat)

    @time_and_log
    def add_data(self, input_directory, output_directory, auto_register):
        """Add a data settings.

        This function converts a DICOM directory of files to .nii.gz files.
        Optionally adds them to the settings database.

        Args:
            input_directory (str): The directory containing DICOM data.
            output_directory (str): The directory for storing the nii.gz files.
            auto_register (Optional[bool]): Should the created nii.gz files be stored in the settings database.
        """
        self.setValue('input_directory', input_directory)
        self.setValue('output_directory', output_directory)
        if auto_register:
            self.setValue('auto_register', 'true')
        else:
            self.setValue('auto_register', 'false')
        self.sync()

    @time_and_log
    def get_data(self):
        """Get the value of an attribute from the object.

        This function gets the value of an attribute from the object. If the
        attribute does not exist, it returns the default value.

        Args:
            object: The object from which to get the attribute.
            attribute (str): The name of the attribute.
            default: The default value to return if the attribute does not exist.

        Returns:
            The value of the attribute if it exists, otherwise the default value.
        """
        if not self.contains('input_directory'):
            return '.', '.', False
        input_directory = self.value('input_directory')
        output_directory = self.value('output_directory')
        auto_register_str = self.value('auto_register')
        if auto_register_str == 'true':
            auto_register = True
        else:
            auto_register = False
        return input_directory, output_directory, auto_register
