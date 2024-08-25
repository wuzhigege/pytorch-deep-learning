{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8a6b002e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T05:33:18.927565Z",
     "iopub.status.busy": "2024-08-25T05:33:18.926358Z",
     "iopub.status.idle": "2024-08-25T05:33:27.646829Z",
     "shell.execute_reply": "2024-08-25T05:33:27.645474Z"
    },
    "papermill": {
     "duration": 8.726457,
     "end_time": "2024-08-25T05:33:27.649171",
     "exception": false,
     "start_time": "2024-08-25T05:33:18.922714",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cloning into 'Show-o'...\r\n",
      "remote: Enumerating objects: 234, done.\u001b[K\r\n",
      "remote: Counting objects: 100% (94/94), done.\u001b[K\r\n",
      "remote: Compressing objects: 100% (55/55), done.\u001b[K\r\n",
      "remote: Total 234 (delta 48), reused 79 (delta 39), pack-reused 140 (from 1)\u001b[K\r\n",
      "Receiving objects: 100% (234/234), 52.93 MiB | 22.34 MiB/s, done.\r\n",
      "Resolving deltas: 100% (83/83), done.\r\n",
      "Repository cloned and compressed successfully.\n"
     ]
    }
   ],
   "source": [
    "!git clone https://github.com/wuzhigege/Show-o.git\n",
    "\n",
    "import shutil\n",
    "import os\n",
    "\n",
    "# Path to the cloned repository\n",
    "repo_path = \"/kaggle/working/Show-o\"\n",
    "\n",
    "# Compress the repository\n",
    "archive_path = \"/kaggle/working/Show-o.zip\"\n",
    "shutil.make_archive(\"Show-o\", \"zip\", repo_path)\n",
    "\n",
    "print(\"Repository cloned and compressed successfully.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c7eeafb2",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T05:33:27.657245Z",
     "iopub.status.busy": "2024-08-25T05:33:27.656829Z",
     "iopub.status.idle": "2024-08-25T05:33:27.937427Z",
     "shell.execute_reply": "2024-08-25T05:33:27.935922Z"
    },
    "papermill": {
     "duration": 0.28764,
     "end_time": "2024-08-25T05:33:27.940104",
     "exception": false,
     "start_time": "2024-08-25T05:33:27.652464",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PDF downloaded successfully as 2408.12528v1.pdf\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "# URL of the PDF on arXiv\n",
    "pdf_url = 'https://arxiv.org/pdf/2408.12528v1.pdf'\n",
    "\n",
    "# Local file name to save the PDF as\n",
    "local_filename = '2408.12528v1.pdf'\n",
    "\n",
    "# Send a GET request to the PDF URL\n",
    "response = requests.get(pdf_url)\n",
    "\n",
    "# Check if the request was successful\n",
    "if response.status_code == 200:\n",
    "    # Write the content of the response to a local file\n",
    "    with open(local_filename, 'wb') as file:\n",
    "        file.write(response.content)\n",
    "    print(f'PDF downloaded successfully as {local_filename}')\n",
    "else:\n",
    "    print(f'Failed to download PDF. Status code: {response.status_code}')"
   ]
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "none",
   "dataSources": [],
   "dockerImageVersionId": 30761,
   "isGpuEnabled": false,
   "isInternetEnabled": true,
   "language": "python",
   "sourceType": "notebook"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.14"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 12.437658,
   "end_time": "2024-08-25T05:33:28.364072",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2024-08-25T05:33:15.926414",
   "version": "2.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
