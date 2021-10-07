##This script imports datasets from the Leukemia Classification challenge directly from Kaggle into Google Colab.
! pip install -q kaggle

#Upload API token file downloaded from Kaggle
from google.colab import files
files.upload()

#Make a new directory and copy API token file into directory
! mkdir ~/.kaggle
! cp kaggle.json ~/.kaggle/

#Change permission of file
! chmod 600 ~/.kaggle/kaggle.json
! kaggle datasets list

#Download datasets from Leukaemia challenge
#! kaggle datasets download -d andrewmvd/leukemia-classification

#Make directory to unzip and store downloaded datasets
! mkdir datasets
! unzip leukemia-classification.zip -d datasets