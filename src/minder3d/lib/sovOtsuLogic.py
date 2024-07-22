import itk
import numpy as np


class OtsuLogic:
    def fix_mask(self, mask_img):
        mask_arr = itk.GetArrayFromImage(mask_img)
        mask_values = np.unique(mask_arr)

        new_mask_arr = mask_arr.copy()

        for i in range(len(mask_values)):
            indexes = np.where(mask_arr == mask_values[i])
            new_mask_arr[indexes] = i
        corner_value = new_mask_arr[0, 0, 0]
        if corner_value != 0:
            indexes_wrong_bg = np.where(new_mask_arr == 0)
            indexes_wrong_fg = np.where(new_mask_arr == corner_value)
            new_mask_arr[indexes_wrong_bg] = corner_value
            new_mask_arr[indexes_wrong_fg] = 0

        new_img = itk.GetImageFromArray(new_mask_arr)
        new_img.CopyInformation(mask_img)

        return new_img

    def run(self, inputImage, numberOfThresholds):
        if numberOfThresholds <= 1:
            filter = itk.OtsuThresholdImageFilter.New(Input=inputImage)
            filter.Update()
            return self.fix_mask(filter.GetOutput().astype(np.uint8))
        else:
            filter = itk.OtsuMultipleThresholdsImageFilter.New(Input=inputImage)
            filter.SetNumberOfThresholds(numberOfThresholds)
            filter.Update()

            return self.fix_mask(filter.GetOutput().astype(np.uint8))
