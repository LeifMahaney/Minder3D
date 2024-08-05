# Minder3D

Using AI to foster innovation in the exploration of radiological images.

## Installing in a end-user system (without a python already installed)

Download the installation package for current release from
    [work-in-progress]

## Installing and Running in a Python Environment

    pip install minder3d

## Running

    minder3d

## Installing the Development Environment

Create a virtual environment

    python3 -m venv venv

Activate that environment, proper syntax depends on platform.  For linux

    source venv/bin/activate

For windows running gitbash

    . ./venv/scripts/activate

Install the test-build of ITK, ITKMinimalPathExtraction ITKTubetk:

    python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ --upgrade itk itk-minimalpathextraction itk-tubetk

Get the Minder3D source code

    git clone https://github.com/aylward/Minder3D

Setup for editable installation. Changes to code in src are
immediatelly reflected in the installed version.  Also installs
all dependencies needed for development and testing:

    cd Minder3D
    pip install -e .[dev]

Prior to making a commit, please verify your code is compliant:

    pre-commit run --all-files

## HINTS

QT Designer was used to define the layout.  On Windows, to launch
designer, use this command:

    qt6-tools.exe designer pytubeview.ui
