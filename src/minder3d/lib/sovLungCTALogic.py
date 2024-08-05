import importlib.util as imp
import subprocess
import sys

import itk
import numpy as np

from .sovImageProcessLogic import ImageProcessLogic
from .sovUtils import time_and_log

label_mapping = {
1:	'spleen',
2:	'kidney_right',	
3:	'kidney_left',
4:	'gallbladder',
5:	'liver',
6:	'stomach',
7:	'pancreas',
8:	'adrenal_gland_right',
9:	'adrenal_gland_left',
10:	'lung_upper_lobe_left',
11:	'lung_lower_lobe_left',
12:	'lung_upper_lobe_right',
13:	'lung_middle_lobe_right',
14:	'lung_lower_lobe_right',
15:	'esophagus',
16:	'trachea',
17:	'thyroid_gland',
18:	'small_bowel',
19:	'duodenum',
20:	'colon',
21:	'urinary_bladder',
22:	'prostate',
23:	'kidney_cyst_left',
24:	'kidney_cyst_right',
25:	'sacrum',
26:	'vertebrae_S1',
27:	'vertebrae_L5',
28:	'vertebrae_L4',
29:	'vertebrae_L3',
30:	'vertebrae_L2',
31:	'vertebrae_L1',
32:	'vertebrae_T12',
33:	'vertebrae_T11',
34:	'vertebrae_T9',
36:	'vertebrae_T8',
37:	'vertebrae_T7',
38:	'vertebrae_T6',
39:	'vertebrae_T5',
40:	'vertebrae_T3',
42:	'vertebrae_T2',
43:	'vertebrae_T1',
44:	'vertebrae_C7',
45:	'vertebrae_C6',
46:	'vertebrae_C5',
47:	'vertebrae_C4',
48:	'vertebrae_C3',
49:	'vertebrae_C2',
50:	'vertebrae_C1',
51:	'heart',
52:	'aorta',
53:	'pulmonary_vein',
54:	'brachiocephalic_trunk',
55:	'subclavian_artery_right',
56:	'subclavian_artery_left',
57:	'common_carotid_artery_right',
58:	'common_carotid_artery_left',
59:	'brachiocephalic_vein_left',
60:	'brachiocephalic_vein_right',
61:	'atrial_appendage_left',
62:	'superior_vena_cava',
63:	'inferior_vena_cava',
64:	'portal_vein_and_splenic_vein',
65:	'iliac_artery_left',
66:	'iliac_artery_right',
67:	'iliac_vena_left',
68:	'iliac_vena_right',
69:	'humerus_left',
70:	'humerus_right',
71:	'scapula_left',
72:	'scapula_right',
73:	'clavicula_left',
74:	'clavicula_right',
75:	'femur_left',
76:	'femur_right',
77:	'hip_left',
78:	'hip_right',
79:	'spinal_cord',
80:	'gluteus_maximus_left',
81:	'gluteus_maximus_right',
82:	'gluteus_medius_left',
83:	'gluteus_medius_right',
84:	'gluteus_minimus_left',
85:	'gluteus_minimus_right',
86:	'autochthon_left',
87:	'autochthon_right',
88:	'iliopsoas_left',
89:	'iliopsoas_right',
90:	'brain',
91:	'skull',
92:	'rib_left_1',
93:	'rib_left_2',
94:	'rib_left_3',
95:	'rib_left_4',
96:	'rib_left_5',
97:	'rib_left_6',
98:	'rib_left_7',
99:	'rib_left_8',
100:'rib_left_9',
101:'rib_left_10',
102:'rib_left_11',
103:'rib_left_12',
104:'rib_right_1',
105:'rib_right_2',
106:'rib_right_3',
107:'rib_right_4',
108:'rib_right_5',
109:'rib_right_6',
110:'rib_right_7',
111:'rib_right_8',
112:'rib_right_9',
113:'rib_right_10',
114:'rib_right_11',
115:'rib_right_12',
116:'sternum',
117:'costal_cartilages'
}

class LungCTALogic:
    def __init__(self):
        self.ai_first_run = True
        self.image = None
        self.pre_image = None
        self.mask = None
        self.voxel_volume = None
    
    def get_voxel_volume(self):
        if self.voxel_volume is None:
            raise ValueError('Initialize Voxel Volume')
        return self.voxel_volume

    def number_of_voxels(self, segmented_image, label, min_voxels = 5):
        array = itk.GetArrayFromImage(segmented_image)
        num_voxels = np.sum(array == label)
        return num_voxels >= min_voxels
    
    def calculate_volume(self, segmented_image, label_name):
        label = label_mapping[label_name]
        l3_label = label_mapping[29]

    # Convert ITK image to NumPy array once
        image_array = itk.GetArrayFromImage(segmented_image)
        l3_array = image_array == l3_label
        psoas_array = image_array == label

    # Debug: Print shapes and sums of arrays
        print(f"l3_array shape: {l3_array.shape}, sum: {np.sum(l3_array)}")
        print(f"psoas_array shape: {psoas_array.shape}, sum: {np.sum(psoas_array)}")

    # Identify sufficient slices based on z-axis (0-th dimension)
        sufficient_slices = np.sum(l3_array, axis=(1, 2)) >= 5
        print(f"sufficient_slices shape: {sufficient_slices.shape}, sum: {np.sum(sufficient_slices)}")

    # Apply mask to select sufficient slices
        psoas_array = psoas_array[sufficient_slices]
        print(f"psoas_array after slicing shape: {psoas_array.shape}, sum: {np.sum(psoas_array)}")

        voxel_volume = self.get_voxel_volume()
        num_voxels = np.sum(psoas_array)
        volume = num_voxels * voxel_volume

    # Debug: Print final volume calculation
        print(f"num_voxels: {num_voxels}, voxel_volume: {voxel_volume}, volume: {volume}")

        return volume

    
    def calculate_two_volumes(self, segmented_image, label_name1, label_name2):
        label1 = label_mapping[label_name1]
        label2 = label_mapping[label_name2]
        l3_label = label_mapping[29]

    # Debug: Check if labels are correctly mapped
        print(f"Label 1: {label1}, Label 2: {label2}, L3 Label: {l3_label}")

    # Convert ITK image to NumPy array once
        image_array = itk.GetArrayFromImage(segmented_image)
        l3_array = image_array == l3_label
        region1_array = image_array == label1
        region2_array = image_array == label2

    # Debug: Check the shapes and sum of arrays before slicing
        print(f"L3 array shape: {l3_array.shape}, sum: {np.sum(l3_array)}")
        print(f"Region 1 array shape: {region1_array.shape}, sum: {np.sum(region1_array)}")
        print(f"Region 2 array shape: {region2_array.shape}, sum: {np.sum(region2_array)}")

    # Identify sufficient slices based on z-axis (0-th dimension)
        sufficient_slices = np.sum(l3_array, axis=(1, 2)) >= 5
        print(f"Sufficient slices: {sufficient_slices.shape}, sum: {np.sum(sufficient_slices)}")

    # Apply mask to select sufficient slices
        region1_array = region1_array[sufficient_slices]
        region2_array = region2_array[sufficient_slices]

    # Debug: Check the shapes and sum of arrays after slicing
        print(f"Region 1 array after slicing shape: {region1_array.shape}, sum: {np.sum(region1_array)}")
        print(f"Region 2 array after slicing shape: {region2_array.shape}, sum: {np.sum(region2_array)}")

        voxel_volume = self.get_voxel_volume()
        num_voxels1 = np.sum(region1_array)
        num_voxels2 = np.sum(region2_array)

    # Debug: Check the number of voxels calculated
        print(f"Number of voxels in region 1: {num_voxels1}")
        print(f"Number of voxels in region 2: {num_voxels2}")

        volume1 = num_voxels1 * voxel_volume
        volume2 = num_voxels2 * voxel_volume

    # Debug: Check the volumes calculated
        print(f"Volume 1: {volume1}")
        print(f"Volume 2: {volume2}")

        return volume1, volume2


    # Seperates the image into two regions based on specific parameters which include 
    def split_into_two_regions(self, segmented_image, label1, label2):
        array = itk.GetArrayFromImage(segmented_image)
        region1 = array == label1
        region2 = array == label2
        region1_img = itk.GetImageFromArray(region1.astype(np.uint8))
        region2_img = itk.GetImageFromArray(region2.astype(np.uint8))
        region1_img.CopyInformation(segmented_image)
        region2_img.CopyInformation(segmented_image)
        return region1_img, region2_img
    
    # Sum of the voxel values in the selected region
    def calculate_calcium_score(self, segmented_image):
        calcium_score = np.sum(itk.GetArrayFromImage(segmented_image))
        return calcium_score
    
    # Average of the voxel values in the segmented image
    def calculate_bmd(self, segmented_image, label_name):
        label = label_mapping[label_name]
        array = itk.GetArrayFromImage(segmented_image)
        bone_region = array == label
        bmd = np.mean(array[bone_region])
        return bmd

    
    @time_and_log
    def initialize(self, image):
        """Initialize the AI model with the given image.

        This method initializes the AI model with the given image. It first checks for the presence of required dependencies and GPU support, and then sets the input image for further processing.

        Args:
            image: The input image for initializing the AI model.

        Returns:
            tuple: A tuple containing the status of initialization (bool), a message (str), and a flag to ask for user confirmation (bool).
        """

        if self.ai_first_run and imp.find_spec('totalsegmentator') is None:
            self.ai_first_run = False
            status = False
            msg = 'This method works best with NVidia GPUs.\nFirst install CUDA (https://developer.nvidia.com/cuda-downloads)\nand then install PyTorch (https://pytorch.org/get-started/locally/)'
            ask_to_continue = False
            return status, msg, ask_to_continue

        if imp.find_spec('torch') is None:
            status = False
            msg = 'PyTorch not found:\nFirst install CUDA (https://developer.nvidia.com/cuda-downloads)\nand then PyTorch (https://pytorch.org/get-started/locally/)'
            ask_to_continue = False
            return status, msg, ask_to_continue

        import torch

        if not torch.cuda.is_available():
            status = False
            msg = 'WARNING: PyTorch installed without CUDA support.\nThe AI methods will run on the CPU and be very slow.\nContinue?'
            ask_to_continue = True
            return status, msg, ask_to_continue

        self.image = image

        spacing = self.image.GetSpacing()
        self.voxel_volume = spacing[0] * spacing[1] * spacing[2]

        status = True
        msg = ''
        ask_to_continue = False
        return status, msg, ask_to_continue

    def preprocess(self):
        """Preprocesses the input image for further analysis.

        If the input image is None, returns None. If the 'totalsegmentator' module is not found, it installs it using pip.
        Then, it checks the spacing of the image and if it does not meet the specified conditions, it preprocesses the image
        using ImageProcessLogic.make_iso method with a spacing of 1.5. Otherwise, it uses the original image for preprocessing.

        Returns:
            SimpleITK.Image: The preprocessed image.

        Raises:
            subprocess.CalledProcessError: If the installation of 'TotalSegmentator' fails.
        """

        if self.image is None:
            return None

        if imp.find_spec('totalsegmentator') is None:
            subprocess.check_call(
                [sys.executable, '-m', 'pip', 'install', 'TotalSegmentator']
            )

        spacing = self.image.GetSpacing()
        if not (
            spacing[0] == 1.5
            and spacing[0] == spacing[1]
            and spacing[1] == spacing[2]
        ):
            preproc = ImageProcessLogic()
            self.pre_image = preproc.make_iso(self.image, 1.5)
        else:
            self.pre_image = self.image
        return self.pre_image

    def run(self, selected_task):
        """Perform image preprocessing and segmentation using the TotalSegmentator library.

        If the pre_image is not provided, it will be preprocessed before segmentation.
        The preprocessing step includes converting the input image to a NIfTI format and applying a transformation matrix.

        Returns:
            itk.Image: The segmented image after preprocessing and segmentation.
        """

        if self.pre_image is None:
            self.preprocess()
            if self.pre_image is None:
                return None

        import nibabel as nib
        from totalsegmentator.python_api import totalsegmentator
        
        pre_array = itk.GetArrayFromImage(self.pre_image)


        pre_array = pre_array.transpose((2, 1, 0))
        mat = np.eye(4)
        mat = mat * 1.5
        mat[3, 3] = 1
        nifti_nib = nib.Nifti1Image(
            np.transpose(pre_array, (2, 1, 0)).copy(), mat
        )
        seg_nib = totalsegmentator(
            input=nifti_nib, output=None, task= selected_task
        )

        seg_array = seg_nib.get_fdata().astype(np.uint8)
        seg_image = itk.GetImageFromArray(
            np.transpose(seg_array, (2, 1, 0)).copy()
        )
        seg_image.CopyInformation(self.pre_image)

        return seg_image
