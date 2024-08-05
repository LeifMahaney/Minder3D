body_parts = {
        "Cancer Survival":['Psoas muscle at L3', 'Visceral vs. subcutaneous'],
        "Cardiac":['Calcium Score', 'Visceral vs. subcutaneous'],
        "Fracture":['target bone'],
        "Organ":['spleen', 'kidney_right', 'kidney_left', 'gallbladder', 'liver', 'stomach', 'pancreas', 'adrenal_gland_right (suprarenal gland)', 'adrenal_gland_left (suprarenal gland)', 'lung_upper_lobe_left (superior lobe of left lung)', 'lung_lower_lobe_left (inferior lobe of left lung)', 'lung_upper_lobe_right (superior lobe of right lung)', 'lung_middle_lobe_right (middle lobe of right lung)', 'lung_lower_lobe_right (inferior lobe of right lung)', 'esophagus', 'trachea', 'thyroid_gland', 'small_bowel (small intestine)', 'duodenum', 'colon', 'urinary_bladder', 'prostate', 'kidney_cyst_left', 'kidney_cyst_right', 'heart, aorta']
    }

cancer_survival_statistical_data = ['Volume', 'Two Volumes']
cardiac_statistical_data = ['Two Volumes', 'Agaston or Equivalent Calcium Score']
fracture_statistical_data = ['Bone Mineral Density', 'Texture Analysis']
organ_statistical_data = ['Volume', 'Texture Analysis']

tasks = ['total', 'lung_vessels', 'cerebral_bleed', 'hip_implant', 'coronary_arteries', 'pleural_pericard_effusion', 'appendicular_bones', 'tissue_types', 'heartchambers_highres', 'face', 'vertebrae_body', 'total_mr', 'tissue_types_mr', 'face_mr']

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QMessageBox, QComboBox, QFileDialog
from PySide6.QtCore import Qt
import sys
from .sovLungCTALogic import LungCTALogic
from .sovUtils import add_objects_in_mask_image_to_scene, time_and_log
from .ui_sovLungCTAPanelWidget import Ui_LungCTAPanelWidget


class LungCTAPanelWidget(QWidget):
    def __init__(self, gui, state, body_parts, cancer_survival_statistical_data, cardiac_statistical_data, fracture_statistical_data, organ_statistical_data, tasks, parent=None):
        super().__init__(parent)
        self.gui = gui
        self.state = state
        self.body_parts = body_parts
        self.cancer_survival_statistcal_data = cancer_survival_statistical_data
        self.cardiac_statistical_data = cardiac_statistical_data
        self.fracture_statistical_data = fracture_statistical_data
        self.organ_statistical_data = organ_statistical_data
        self.tasks = tasks
        self.logic = LungCTALogic()
        self.setWindowTitle("Tool for Segmentation")
        self.main_layout = QVBoxLayout(self)
        self.selected_category = None
        self.seg_image = None
        self.init_ui()

    def calculate_statistics(self):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file_path, _ = QFileDialog.getSaveFileName(self, 'Save calculation as', '', 'Text Files (*.txt);;All Files (*)', options=options)
            if not file_path:
                QMessageBox.warning(self, 'No file selected', 'Please select a file you would like to use')
                return
    
            statistics = []
            category = self.selected_category
            body_part = self.body_part_combobox.currentText()
            target_statistic = self.target_body_part_combobox.currentText()
            self.calculate_button.setVisible(True)
            
            if self.selected_category == 'Cancer Survival':
                if body_part == 'Psoas muscle at L3':
                    if target_statistic == "Volume":
                        volume_left = self.logic.calculate_volume(self.seg_image, 88)
                        volume_right = self.logic.calculate_volume(self.seg_image, 89)
                        statistics.append(f'Volume of iliopsoas Left: {volume_left:.2f}')
                        statistics.append(f'Volume of iliopsoas Right: {volume_right:.2f}')
                    elif target_statistic == "Two Volumes":
                        volume1, volume2 = self.logic.calculate_two_volumes(self.seg_image, 88, 89)
                        statistics.append(f'Volumes: {volume1: .2f} and {volume2: .2f}')  
                elif body_part == 'Visceral vs. subcutaneous':
                    if target_statistic == 'Volume':
                        volume_visceral = self.logic.calculate_volume(self.seg_image, 'visceral_fat')
                        volume_subcutaneous = self.logic.calculate_volume(self.seg_image, 'subcutaneous_fat')
                        statistics.append(f'Volume of visceral Fat: {volume_visceral:.2f}')
                        statistics.append(f'Volume of subcutaneous Fat: {volume_subcutaneous:.2f}')
                    elif target_statistic == 'Two Volumes':
                        volume1, volume2 = self.logic.calculate_two_volumes(self.seg_image, 'visceral_fat', 'subcutaneous_fat')
                        statistics.append(f'Volumes: {volume1:.2f} and {volume2:.2f}')
            if self.selected_category == 'Cardiac':
                if body_part == 'Calcium Score':
                    calcium_score = self.logic.calculate_calcium_score(self.seg_image)
                    statistics.append(f'Calcium Score: {calcium_score:.2f}')
                elif body_part == 'Visceral vs. subcutaneous': 
                    if target_statistic == "Two Volumes":
                        volume1, volume2 = self.logic.calculate_two_volumes(self.seg_image, 'visceral_fat', 'subcutaneous_fat')
                        statistics.append(f'Volumes: {volume1: .2f} and {volume2: .2f}')
                    elif target_statistic == "Agaston or Equivalent Calcium Score":
                        calcium_score = self.logic.calculate_calcium_score(self.seg_image)
                        statistics.append(self, 'Calcium Score', f'Calcium Score: {calcium_score: .2f}')
            if self.selected_category == 'Fracture':
                if body_part == 'target bone':
                    if target_statistic == 'Bone Mineral Density':
                        bmd, texture_features = self.logic.calculate_bmd(self.seg_image, body_part)
                        statistics.append(f'Bone Mineral Density of {body_part} is: {bmd: .2f}')
                    elif target_statistic == 'Texture Analysis':
                        texture_features = self.logic.calculate_texture_analysis(self.seg_image)
                        statistics.append(self, 'Texture Analysis', f'Texture Analysis: {texture_features}')
            if self.selected_category == 'Organ':
                if target_statistic == "Volume":
                    volume = self.logic.calculate_volume(self.seg_image, body_parts)
                    statistics.append(f'volume: {volume:.2f}')
                elif target_statistic == 'Texture Analysis':
                    texture_features = self.logic.calculate_texture_analysis(self.seg_image)
                    statistics.append(f'Texture Analysis: {texture_features}')
            
            message = '\n'.join(statistics)
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(message)
            msg_box.setWindowTitle("Statistics Calculation")
            msg_box.setStandardButtons(QMessageBox.Save | QMessageBox.Close)
            result = msg_box.exec_()

            if result == QMessageBox.Save:
                file_path, _ = QFileDialog.getSaveFileName(self, 'Save calculation as', '', 'Text Files (*.txt);;All Files (*)')
                if file_path:            
                    with open(file_path, 'w') as file:
                        for calculation in statistics:
                            file.write(calculation + '\n')

            QMessageBox.information(self, 'Calculations have been saved', f'Calulations have been saved to {file_path}')


    @time_and_log   
    # Initialize button to select which category
    def init_ui(self):
        self.category_label = QLabel("Select Organ Level:")
        self.main_layout.addWidget(self.category_label)
        self.category_label.setVisible(True)
        self.category_buttons = {}
        
        # Creates a button for each available category
        for category in self.body_parts.keys():
            category_button = QPushButton(category)
            category_button.clicked.connect(lambda checked, cats = category: self.show_body_parts(cats))
            self.main_layout.addWidget(category_button)
            self.category_buttons[category] = category_button
            category_button.setVisible(False)
        
        # Initiates a dropdown for possible tasks
        self.task_combobox = QComboBox()
        self.task_combobox.addItems(self.tasks)
        self.main_layout.addWidget(self.task_combobox)

        # Initiates the segmentation process
        self.segment_button = QPushButton("Segmentate")
        self.segment_button.clicked.connect(self.segment)
        self.segment_button.setVisible(True)
        self.main_layout.addWidget(self.segment_button)


        # Allows the user to pick a body part from the avaible options does not become avaible until the category has been selected
        self.body_part_combobox = QComboBox()
        self.body_part_combobox.currentIndexChanged.connect(self.show_target_body_part_dropdown)
        self.body_part_combobox.setVisible(False)
        self.main_layout.addWidget(self.body_part_combobox)

        # Allows the user to pick the target body part (statistic they want to calculate) from the provided options. Does not become available until the category has been selected
        self.target_body_part_combobox = QComboBox()
        self.target_body_part_combobox.setVisible(False)
        self.main_layout.addWidget(self.target_body_part_combobox)

        # Initiates the claculation for the statisitics selected
        self.calculate_button = QPushButton('Calculate Statistics')
        self.calculate_button.clicked.connect(self.calculate_statistics)
        self.calculate_button.setVisible(False)
        self.main_layout.addWidget(self.calculate_button)

        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.status_label)
    
    # Shows the body parts specific to the category selected
    def show_body_parts(self, category):
        self.selected_category = category
        for button in self.category_buttons.values():
            button.setVisible(False)
        self.body_part_combobox.clear()
        self.body_part_combobox.addItems(body_parts[category])
        self.body_part_combobox.setVisible(True)
        self.target_body_part_combobox.setVisible(True)
        self.segment_button.setVisible(False)
        self.calculate_button.setVisible(True)
        
    # Shows the avaible statistics to calculate based off of the previous selections
    def show_target_body_part_dropdown(self):
        self.target_body_part_combobox.clear()
        if self.selected_category == 'Cancer Survival':
            self.target_body_part_combobox.addItems(self.cancer_survival_statistcal_data)
        elif self.selected_category == 'Cardiac':
            self.target_body_part_combobox.addItems(self.cardiac_statistical_data)
        elif self.selected_category == 'Fracture':
            self.target_body_part_combobox.addItems(self.fracture_statistical_data)
        elif self.selected_category == 'Organ':
            self.target_body_part_combobox.addItems(self.organ_statistical_data)
        self.target_body_part_combobox.setVisible(True)
        self.calculate_button.setVisible(True)


   # Runs the segmentation process
    def segment(self):
        status, msg, ask_to_continue = self.logic.initialize(
            self.state.image[self.state.current_image_num]
        )
        if status is False:
            message = QMessageBox()
            message.setWindowTitle('Verifying AI installation...')
            message.setText(msg)
            if ask_to_continue:
                message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            message.exec()
            if ask_to_continue:
                ret = message.exec()
                if ret == QMessageBox.No:
                    return
            else:
                return

        self.gui.log('Preprocessing...')
        pre_image = self.logic.preprocess()

        self.gui.create_new_image(pre_image, None, 'Iso')
        self.gui.update_image()

        self.gui.log('Running...')
        selected_task = self.task_combobox.currentText()
        self.seg_image = self.logic.run(selected_task)


        self.gui.log('Done.')

        add_objects_in_mask_image_to_scene(self.seg_image, self.state.scene)
        self.gui.update_scene()


        self.task_combobox.setVisible(False)
        self.body_part_combobox.setVisible(False)
        self.target_body_part_combobox.setVisible(False)

        self.segment_button.setVisible(False)
        self.category_label.setVisible(True)
        for button in self.category_buttons.values():
            button.setVisible(True)

        # Update the status label with the selections that have been made
        self.status_label.setText(f"Segmentation process complete. Please select a category for statistical analysis")

        # Call Segmentation using the parameters selected 
        if self.seg_image:
            QMessageBox.information(self, "Segmentation Done", f"Segmentation is complete.")
        else:
            QMessageBox.warning(self, "Segmentation Failed", f'The segmentation process failed.')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Segmentation Tool")
        self.setCentralWidget(LungCTAPanelWidget(gui = None, state = None, body_parts = body_parts, cancer_survival_statistical_data = cancer_survival_statistical_data, cardiac_statistical_data =cardiac_statistical_data, fracture_statistical_data = fracture_statistical_data, organ_statistical_data = organ_statistical_data))

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
