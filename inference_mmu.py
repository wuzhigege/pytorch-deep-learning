{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "41cec3a9",
   "metadata": {
    "papermill": {
     "duration": 0.012797,
     "end_time": "2024-08-25T16:03:41.372736",
     "exception": false,
     "start_time": "2024-08-25T16:03:41.359939",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# download github repo from link fastly"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "681834ce",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:03:41.396572Z",
     "iopub.status.busy": "2024-08-25T16:03:41.396115Z",
     "iopub.status.idle": "2024-08-25T16:03:48.681688Z",
     "shell.execute_reply": "2024-08-25T16:03:48.680025Z"
    },
    "papermill": {
     "duration": 7.300747,
     "end_time": "2024-08-25T16:03:48.684505",
     "exception": false,
     "start_time": "2024-08-25T16:03:41.383758",
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
      "Receiving objects: 100% (234/234), 52.93 MiB | 41.18 MiB/s, done.\r\n",
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
   "id": "8596312f",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:03:48.713316Z",
     "iopub.status.busy": "2024-08-25T16:03:48.712045Z",
     "iopub.status.idle": "2024-08-25T16:03:48.730318Z",
     "shell.execute_reply": "2024-08-25T16:03:48.729133Z"
    },
    "papermill": {
     "duration": 0.035476,
     "end_time": "2024-08-25T16:03:48.733039",
     "exception": false,
     "start_time": "2024-08-25T16:03:48.697563",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Repository cloned and compressed successfully.\n"
     ]
    }
   ],
   "source": [
    "# Path to the cloned repository\n",
    "repo_path2 = \"/kaggle/working/Show-o/models\"\n",
    "\n",
    "# Compress the repository\n",
    "archive_path = \"/kaggle/working/Show-o-models.zip\"\n",
    "shutil.make_archive(\"Show-o-models\", \"zip\", repo_path2)\n",
    "\n",
    "print(\"Repository cloned and compressed successfully.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ca678b7e",
   "metadata": {
    "papermill": {
     "duration": 0.012341,
     "end_time": "2024-08-25T16:03:48.758061",
     "exception": false,
     "start_time": "2024-08-25T16:03:48.745720",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# download pdf from link fastly"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "708ae337",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:03:48.785723Z",
     "iopub.status.busy": "2024-08-25T16:03:48.785262Z",
     "iopub.status.idle": "2024-08-25T16:03:49.068205Z",
     "shell.execute_reply": "2024-08-25T16:03:49.066863Z"
    },
    "papermill": {
     "duration": 0.299752,
     "end_time": "2024-08-25T16:03:49.070944",
     "exception": false,
     "start_time": "2024-08-25T16:03:48.771192",
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
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2c274518",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:03:49.098686Z",
     "iopub.status.busy": "2024-08-25T16:03:49.098128Z",
     "iopub.status.idle": "2024-08-25T16:03:52.463304Z",
     "shell.execute_reply": "2024-08-25T16:03:52.462040Z"
    },
    "papermill": {
     "duration": 3.381752,
     "end_time": "2024-08-25T16:03:52.465759",
     "exception": false,
     "start_time": "2024-08-25T16:03:49.084007",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "import torch\n",
    "print(torch.version.cuda)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "70c25a68",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:03:52.493940Z",
     "iopub.status.busy": "2024-08-25T16:03:52.493334Z",
     "iopub.status.idle": "2024-08-25T16:03:54.457839Z",
     "shell.execute_reply": "2024-08-25T16:03:54.456508Z"
    },
    "papermill": {
     "duration": 1.981295,
     "end_time": "2024-08-25T16:03:54.460465",
     "exception": false,
     "start_time": "2024-08-25T16:03:52.479170",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "torch version: 2.4.0+cpu\n",
      "torchvision version: 0.19.0+cpu\n"
     ]
    }
   ],
   "source": [
    "import torch\n",
    "import torchvision\n",
    "torch.__version__#.split(\".\")\n",
    "assert int(torch.__version__.split(\".\")[1])>=4, \"torch version is bigger than 2.4.0\"\n",
    "assert int(torchvision.__version__.split(\".\")[1])>=19, \"torchversion version is bigger than 0.19.0\"\n",
    "print(f\"torch version: {torch.__version__}\")\n",
    "print(f\"torchvision version: {torchvision.__version__}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e2d162f3",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:03:54.488506Z",
     "iopub.status.busy": "2024-08-25T16:03:54.487914Z",
     "iopub.status.idle": "2024-08-25T16:03:54.499529Z",
     "shell.execute_reply": "2024-08-25T16:03:54.498215Z"
    },
    "papermill": {
     "duration": 0.028575,
     "end_time": "2024-08-25T16:03:54.502100",
     "exception": false,
     "start_time": "2024-08-25T16:03:54.473525",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "torch version: 2.4.0+cpu\n",
      "torchvision version: 0.19.0+cpu\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    import torch\n",
    "    import torchvision\n",
    "\n",
    "    assert int(torch.__version__.split(\".\")[1])>=4, \"torch version is bigger than 2.4.0\"\n",
    "    assert int(torchvision.__version__.split(\".\")[1])>=19, \"torchversion version is bigger than 0.19.0\"\n",
    "    print(f\"torch version: {torch.__version__}\")\n",
    "    print(f\"torchvision version: {torchvision.__version__}\")\n",
    "    print(torch.version.cuda)\n",
    "except:\n",
    "    print(f\"[INFO] torch/torchvision versions not as required, installing nightly versions.\")\n",
    "    !pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu123\n",
    "    import torch\n",
    "    import torchvision\n",
    "    print(f\"torch version: {torch.__version__}\")\n",
    "    print(f\"torchvision version: {torchvision.__version__}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "e0cef93e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:03:54.530705Z",
     "iopub.status.busy": "2024-08-25T16:03:54.529648Z",
     "iopub.status.idle": "2024-08-25T16:04:22.694955Z",
     "shell.execute_reply": "2024-08-25T16:04:22.693595Z"
    },
    "papermill": {
     "duration": 28.182781,
     "end_time": "2024-08-25T16:04:22.698049",
     "exception": false,
     "start_time": "2024-08-25T16:03:54.515268",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[INFO] Couldn't find going_modular scripts... downloading them from GitHub.\n",
      "Cloning into 'pytorch-deep-learning'...\r\n",
      "remote: Enumerating objects: 4177, done.\u001b[K\r\n",
      "remote: Counting objects: 100% (142/142), done.\u001b[K\r\n",
      "remote: Compressing objects: 100% (103/103), done.\u001b[K\r\n",
      "remote: Total 4177 (delta 61), reused 104 (delta 38), pack-reused 4035 (from 1)\u001b[K\r\n",
      "Receiving objects: 100% (4177/4177), 651.42 MiB | 41.69 MiB/s, done.\r\n",
      "Resolving deltas: 100% (2432/2432), done.\r\n",
      "Updating files: 100% (248/248), done.\r\n"
     ]
    }
   ],
   "source": [
    "import torch\n",
    "import torchvision\n",
    "import matplotlib.pyplot as plt\n",
    "from torch import nn\n",
    "from torchvision import transforms\n",
    "\n",
    "try:\n",
    "    from torchinfo import summary\n",
    "except:\n",
    "    print(\"please install torchinfo\")\n",
    "    !pip install -q torchinfo\n",
    "    from torchinfo import summary\n",
    "# Try to import the going_modular directory, download it from GitHub if it doesn't work\n",
    "try:\n",
    "    \n",
    "    from foing_modular.going_modular import data_setup,engineer\n",
    "except:\n",
    "    print(\"[INFO] Couldn't find going_modular scripts... downloading them from GitHub.\")\n",
    "    !git clone https://github.com/mrdbourke/pytorch-deep-learning\n",
    "    !mv pytorch-deep-learning/going_modular .\n",
    "    !rm -rf pytorch-deep-learning\n",
    "    from going_modular.going_modular import data_setup,engine"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "dc6884b6",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:04:22.747769Z",
     "iopub.status.busy": "2024-08-25T16:04:22.747287Z",
     "iopub.status.idle": "2024-08-25T16:04:22.753005Z",
     "shell.execute_reply": "2024-08-25T16:04:22.751964Z"
    },
    "papermill": {
     "duration": 0.033283,
     "end_time": "2024-08-25T16:04:22.755532",
     "exception": false,
     "start_time": "2024-08-25T16:04:22.722249",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from going_modular.going_modular import data_setup,engine"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "eb4b5a73",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:04:22.805528Z",
     "iopub.status.busy": "2024-08-25T16:04:22.804659Z",
     "iopub.status.idle": "2024-08-25T16:04:22.814045Z",
     "shell.execute_reply": "2024-08-25T16:04:22.812644Z"
    },
    "papermill": {
     "duration": 0.038022,
     "end_time": "2024-08-25T16:04:22.816854",
     "exception": false,
     "start_time": "2024-08-25T16:04:22.778832",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'cpu'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "device=\"cuda\" if torch.cuda.is_available() else \"cpu\"\n",
    "device"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "732010ac",
   "metadata": {
    "papermill": {
     "duration": 0.023396,
     "end_time": "2024-08-25T16:04:22.863623",
     "exception": false,
     "start_time": "2024-08-25T16:04:22.840227",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## 1. Get data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "3044c13c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:04:22.913857Z",
     "iopub.status.busy": "2024-08-25T16:04:22.912804Z",
     "iopub.status.idle": "2024-08-25T16:04:22.918929Z",
     "shell.execute_reply": "2024-08-25T16:04:22.917658Z"
    },
    "papermill": {
     "duration": 0.033554,
     "end_time": "2024-08-25T16:04:22.921521",
     "exception": false,
     "start_time": "2024-08-25T16:04:22.887967",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import os \n",
    "from pathlib import Path\n",
    "data_path=Path(\"data/\")\n",
    "image_path=data_path/\"pizza_steak_sushi\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "4559d878",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:04:22.970676Z",
     "iopub.status.busy": "2024-08-25T16:04:22.969636Z",
     "iopub.status.idle": "2024-08-25T16:04:23.489836Z",
     "shell.execute_reply": "2024-08-25T16:04:23.488248Z"
    },
    "papermill": {
     "duration": 0.548499,
     "end_time": "2024-08-25T16:04:23.493179",
     "exception": false,
     "start_time": "2024-08-25T16:04:22.944680",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "data/pizza_steak_sushi has downdload.....\n",
      "Unzipping pizza, steak, sushi data...\n"
     ]
    }
   ],
   "source": [
    "import os \n",
    "import zipfile\n",
    "from pathlib import Path\n",
    "import requests\n",
    "# Setup path to data folder\n",
    "data_path=Path(\"data/\")\n",
    "image_path=data_path/\"pizza_steak_sushi\"\n",
    "if image_path.is_dir():\n",
    "    print(f\"{image_path} has existed\")\n",
    "else:\n",
    "    image_path.mkdir(parents=True,exist_ok=True)\n",
    "    print(f\"{image_path} has downdload.....\")\n",
    "    \n",
    "    with open(data_path/\"pizza_steak_sushi.zip\",\"wb\") as f:\n",
    "        request=requests.get(\"https://github.com/mrdbourke/pytorch-deep-learning/raw/main/data/pizza_steak_sushi.zip\")\n",
    "        f.write(request.content)\n",
    "    with zipfile.ZipFile(data_path/\"pizza_steak_sushi.zip\",\"r\") as zip_ref:\n",
    "        print(\"Unzipping pizza, steak, sushi data...\") \n",
    "        zip_ref.extractall(image_path)\n",
    "    os.remove(data_path/\"pizza_steak_sushi.zip\")\n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "41212480",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:04:23.543604Z",
     "iopub.status.busy": "2024-08-25T16:04:23.543076Z",
     "iopub.status.idle": "2024-08-25T16:04:23.551549Z",
     "shell.execute_reply": "2024-08-25T16:04:23.550199Z"
    },
    "papermill": {
     "duration": 0.036747,
     "end_time": "2024-08-25T16:04:23.554075",
     "exception": false,
     "start_time": "2024-08-25T16:04:23.517328",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PosixPath('data/pizza_steak_sushi/train')"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_dir=image_path/\"train\"\n",
    "test_dir=image_path/\"test\"\n",
    "train_dir"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "565f815d",
   "metadata": {
    "papermill": {
     "duration": 0.023277,
     "end_time": "2024-08-25T16:04:23.601273",
     "exception": false,
     "start_time": "2024-08-25T16:04:23.577996",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## 2. Create Datasets and DataLoaders"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8c636607",
   "metadata": {
    "papermill": {
     "duration": 0.023294,
     "end_time": "2024-08-25T16:04:23.647993",
     "exception": false,
     "start_time": "2024-08-25T16:04:23.624699",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### 2.1 Creating a transform for `torchvision.models` (manual creation)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "5652c70e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:04:23.697057Z",
     "iopub.status.busy": "2024-08-25T16:04:23.696519Z",
     "iopub.status.idle": "2024-08-25T16:04:23.704205Z",
     "shell.execute_reply": "2024-08-25T16:04:23.702676Z"
    },
    "papermill": {
     "duration": 0.03545,
     "end_time": "2024-08-25T16:04:23.706762",
     "exception": false,
     "start_time": "2024-08-25T16:04:23.671312",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "manual_transform=transforms.Compose([transforms.Resize(size=(224,224)),\n",
    "                                   transforms.ToTensor(),\n",
    "                                   transforms.Normalize(mean=[0.485, 0.456, 0.406],\n",
    "                         std=[0.229, 0.224, 0.225])])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "1b416a54",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:04:23.757191Z",
     "iopub.status.busy": "2024-08-25T16:04:23.756718Z",
     "iopub.status.idle": "2024-08-25T16:04:23.768941Z",
     "shell.execute_reply": "2024-08-25T16:04:23.767547Z"
    },
    "papermill": {
     "duration": 0.040516,
     "end_time": "2024-08-25T16:04:23.771529",
     "exception": false,
     "start_time": "2024-08-25T16:04:23.731013",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(<torch.utils.data.dataloader.DataLoader at 0x7c16dca5ee00>,\n",
       " <torch.utils.data.dataloader.DataLoader at 0x7c16dd78f1c0>,\n",
       " ['pizza', 'steak', 'sushi'])"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_dataloader,test_dataloader,class_name=data_setup.create_dataloaders(train_dir=train_dir,\n",
    "                                                                         test_dir=test_dir,\n",
    "                                                                         transform=manual_transform,\n",
    "                                                                         batch_size=32)\n",
    "train_dataloader,test_dataloader,class_name"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "33efd443",
   "metadata": {
    "papermill": {
     "duration": 0.025013,
     "end_time": "2024-08-25T16:04:23.820782",
     "exception": false,
     "start_time": "2024-08-25T16:04:23.795769",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### 2.2 Creating a transform for `torchvision.models` (auto creation)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "01957985",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:04:23.870600Z",
     "iopub.status.busy": "2024-08-25T16:04:23.870152Z",
     "iopub.status.idle": "2024-08-25T16:04:23.878984Z",
     "shell.execute_reply": "2024-08-25T16:04:23.877587Z"
    },
    "papermill": {
     "duration": 0.037494,
     "end_time": "2024-08-25T16:04:23.882225",
     "exception": false,
     "start_time": "2024-08-25T16:04:23.844731",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "EfficientNet_B0_Weights.IMAGENET1K_V1"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "weights_6=torchvision.models.EfficientNet_B6_Weights.DEFAULT\n",
    "weights_6\n",
    "weights=torchvision.models.EfficientNet_B0_Weights.DEFAULT\n",
    "weights"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "64da8838",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:04:23.934262Z",
     "iopub.status.busy": "2024-08-25T16:04:23.933752Z",
     "iopub.status.idle": "2024-08-25T16:04:23.942980Z",
     "shell.execute_reply": "2024-08-25T16:04:23.941636Z"
    },
    "papermill": {
     "duration": 0.038046,
     "end_time": "2024-08-25T16:04:23.945979",
     "exception": false,
     "start_time": "2024-08-25T16:04:23.907933",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(ImageClassification(\n",
       "     crop_size=[528]\n",
       "     resize_size=[528]\n",
       "     mean=[0.485, 0.456, 0.406]\n",
       "     std=[0.229, 0.224, 0.225]\n",
       "     interpolation=InterpolationMode.BICUBIC\n",
       " ),\n",
       " ImageClassification(\n",
       "     crop_size=[224]\n",
       "     resize_size=[256]\n",
       "     mean=[0.485, 0.456, 0.406]\n",
       "     std=[0.229, 0.224, 0.225]\n",
       "     interpolation=InterpolationMode.BICUBIC\n",
       " ))"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get the transforms used to create our pretrained weights\n",
    "auto_transforms_6=weights_6.transforms()\n",
    "auto_transforms=weights.transforms()\n",
    "auto_transforms_6,auto_transforms"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "d49b2522",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:04:23.998436Z",
     "iopub.status.busy": "2024-08-25T16:04:23.997980Z",
     "iopub.status.idle": "2024-08-25T16:04:24.010819Z",
     "shell.execute_reply": "2024-08-25T16:04:24.009458Z"
    },
    "papermill": {
     "duration": 0.042217,
     "end_time": "2024-08-25T16:04:24.013530",
     "exception": false,
     "start_time": "2024-08-25T16:04:23.971313",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(<torch.utils.data.dataloader.DataLoader at 0x7c16b9fb1c30>,\n",
       " <torch.utils.data.dataloader.DataLoader at 0x7c16b9fb0d00>,\n",
       " ['pizza', 'steak', 'sushi'])"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train_dataloader,test_dataloader,class_name=data_setup.create_dataloaders(train_dir=train_dir,\n",
    "                                                                         test_dir=test_dir,\n",
    "                                                                         transform=manual_transform,\n",
    "                                                                         batch_size=32)\n",
    "train_dataloader,test_dataloader,class_name"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "10dd7660",
   "metadata": {
    "papermill": {
     "duration": 0.023906,
     "end_time": "2024-08-25T16:04:24.062149",
     "exception": false,
     "start_time": "2024-08-25T16:04:24.038243",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### 3.0 creating a pretrained model"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b94aa6e1",
   "metadata": {
    "papermill": {
     "duration": 0.024123,
     "end_time": "2024-08-25T16:04:24.110508",
     "exception": false,
     "start_time": "2024-08-25T16:04:24.086385",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "### 3.2 Setting up a pretrained model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "793400b5",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:04:24.162017Z",
     "iopub.status.busy": "2024-08-25T16:04:24.161574Z",
     "iopub.status.idle": "2024-08-25T16:04:26.984411Z",
     "shell.execute_reply": "2024-08-25T16:04:26.983281Z"
    },
    "papermill": {
     "duration": 2.852261,
     "end_time": "2024-08-25T16:04:26.987231",
     "exception": false,
     "start_time": "2024-08-25T16:04:24.134970",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Downloading: \"https://download.pytorch.org/models/efficientnet_b6_lukemelas-24a108a5.pth\" to /root/.cache/torch/hub/checkpoints/efficientnet_b6_lukemelas-24a108a5.pth\n",
      "100%|██████████| 165M/165M [00:01<00:00, 138MB/s]\n"
     ]
    }
   ],
   "source": [
    "model_6=torchvision.models.efficientnet_b6(weights=weights_6).to(device)\n",
    "model_6;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "92571d5b",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:04:27.040604Z",
     "iopub.status.busy": "2024-08-25T16:04:27.040151Z",
     "iopub.status.idle": "2024-08-25T16:04:27.494215Z",
     "shell.execute_reply": "2024-08-25T16:04:27.492892Z"
    },
    "papermill": {
     "duration": 0.484541,
     "end_time": "2024-08-25T16:04:27.497644",
     "exception": false,
     "start_time": "2024-08-25T16:04:27.013103",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Downloading: \"https://download.pytorch.org/models/efficientnet_b0_rwightman-7f5810bc.pth\" to /root/.cache/torch/hub/checkpoints/efficientnet_b0_rwightman-7f5810bc.pth\n",
      "100%|██████████| 20.5M/20.5M [00:00<00:00, 119MB/s] \n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "EfficientNet(\n",
       "  (features): Sequential(\n",
       "    (0): Conv2dNormActivation(\n",
       "      (0): Conv2d(3, 32, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)\n",
       "      (1): BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "      (2): SiLU(inplace=True)\n",
       "    )\n",
       "    (1): Sequential(\n",
       "      (0): MBConv(\n",
       "        (block): Sequential(\n",
       "          (0): Conv2dNormActivation(\n",
       "            (0): Conv2d(32, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=32, bias=False)\n",
       "            (1): BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (1): SqueezeExcitation(\n",
       "            (avgpool): AdaptiveAvgPool2d(output_size=1)\n",
       "            (fc1): Conv2d(32, 8, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (fc2): Conv2d(8, 32, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (activation): SiLU(inplace=True)\n",
       "            (scale_activation): Sigmoid()\n",
       "          )\n",
       "          (2): Conv2dNormActivation(\n",
       "            (0): Conv2d(32, 16, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "          )\n",
       "        )\n",
       "        (stochastic_depth): StochasticDepth(p=0.0, mode=row)\n",
       "      )\n",
       "    )\n",
       "    (2): Sequential(\n",
       "      (0): MBConv(\n",
       "        (block): Sequential(\n",
       "          (0): Conv2dNormActivation(\n",
       "            (0): Conv2d(16, 96, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(96, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (1): Conv2dNormActivation(\n",
       "            (0): Conv2d(96, 96, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=96, bias=False)\n",
       "            (1): BatchNorm2d(96, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (2): SqueezeExcitation(\n",
       "            (avgpool): AdaptiveAvgPool2d(output_size=1)\n",
       "            (fc1): Conv2d(96, 4, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (fc2): Conv2d(4, 96, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (activation): SiLU(inplace=True)\n",
       "            (scale_activation): Sigmoid()\n",
       "          )\n",
       "          (3): Conv2dNormActivation(\n",
       "            (0): Conv2d(96, 24, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(24, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "          )\n",
       "        )\n",
       "        (stochastic_depth): StochasticDepth(p=0.0125, mode=row)\n",
       "      )\n",
       "      (1): MBConv(\n",
       "        (block): Sequential(\n",
       "          (0): Conv2dNormActivation(\n",
       "            (0): Conv2d(24, 144, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(144, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (1): Conv2dNormActivation(\n",
       "            (0): Conv2d(144, 144, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=144, bias=False)\n",
       "            (1): BatchNorm2d(144, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (2): SqueezeExcitation(\n",
       "            (avgpool): AdaptiveAvgPool2d(output_size=1)\n",
       "            (fc1): Conv2d(144, 6, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (fc2): Conv2d(6, 144, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (activation): SiLU(inplace=True)\n",
       "            (scale_activation): Sigmoid()\n",
       "          )\n",
       "          (3): Conv2dNormActivation(\n",
       "            (0): Conv2d(144, 24, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(24, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "          )\n",
       "        )\n",
       "        (stochastic_depth): StochasticDepth(p=0.025, mode=row)\n",
       "      )\n",
       "    )\n",
       "    (3): Sequential(\n",
       "      (0): MBConv(\n",
       "        (block): Sequential(\n",
       "          (0): Conv2dNormActivation(\n",
       "            (0): Conv2d(24, 144, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(144, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (1): Conv2dNormActivation(\n",
       "            (0): Conv2d(144, 144, kernel_size=(5, 5), stride=(2, 2), padding=(2, 2), groups=144, bias=False)\n",
       "            (1): BatchNorm2d(144, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (2): SqueezeExcitation(\n",
       "            (avgpool): AdaptiveAvgPool2d(output_size=1)\n",
       "            (fc1): Conv2d(144, 6, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (fc2): Conv2d(6, 144, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (activation): SiLU(inplace=True)\n",
       "            (scale_activation): Sigmoid()\n",
       "          )\n",
       "          (3): Conv2dNormActivation(\n",
       "            (0): Conv2d(144, 40, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(40, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "          )\n",
       "        )\n",
       "        (stochastic_depth): StochasticDepth(p=0.037500000000000006, mode=row)\n",
       "      )\n",
       "      (1): MBConv(\n",
       "        (block): Sequential(\n",
       "          (0): Conv2dNormActivation(\n",
       "            (0): Conv2d(40, 240, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(240, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (1): Conv2dNormActivation(\n",
       "            (0): Conv2d(240, 240, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2), groups=240, bias=False)\n",
       "            (1): BatchNorm2d(240, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (2): SqueezeExcitation(\n",
       "            (avgpool): AdaptiveAvgPool2d(output_size=1)\n",
       "            (fc1): Conv2d(240, 10, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (fc2): Conv2d(10, 240, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (activation): SiLU(inplace=True)\n",
       "            (scale_activation): Sigmoid()\n",
       "          )\n",
       "          (3): Conv2dNormActivation(\n",
       "            (0): Conv2d(240, 40, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(40, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "          )\n",
       "        )\n",
       "        (stochastic_depth): StochasticDepth(p=0.05, mode=row)\n",
       "      )\n",
       "    )\n",
       "    (4): Sequential(\n",
       "      (0): MBConv(\n",
       "        (block): Sequential(\n",
       "          (0): Conv2dNormActivation(\n",
       "            (0): Conv2d(40, 240, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(240, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (1): Conv2dNormActivation(\n",
       "            (0): Conv2d(240, 240, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), groups=240, bias=False)\n",
       "            (1): BatchNorm2d(240, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (2): SqueezeExcitation(\n",
       "            (avgpool): AdaptiveAvgPool2d(output_size=1)\n",
       "            (fc1): Conv2d(240, 10, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (fc2): Conv2d(10, 240, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (activation): SiLU(inplace=True)\n",
       "            (scale_activation): Sigmoid()\n",
       "          )\n",
       "          (3): Conv2dNormActivation(\n",
       "            (0): Conv2d(240, 80, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(80, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "          )\n",
       "        )\n",
       "        (stochastic_depth): StochasticDepth(p=0.0625, mode=row)\n",
       "      )\n",
       "      (1): MBConv(\n",
       "        (block): Sequential(\n",
       "          (0): Conv2dNormActivation(\n",
       "            (0): Conv2d(80, 480, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(480, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (1): Conv2dNormActivation(\n",
       "            (0): Conv2d(480, 480, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=480, bias=False)\n",
       "            (1): BatchNorm2d(480, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (2): SqueezeExcitation(\n",
       "            (avgpool): AdaptiveAvgPool2d(output_size=1)\n",
       "            (fc1): Conv2d(480, 20, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (fc2): Conv2d(20, 480, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (activation): SiLU(inplace=True)\n",
       "            (scale_activation): Sigmoid()\n",
       "          )\n",
       "          (3): Conv2dNormActivation(\n",
       "            (0): Conv2d(480, 80, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(80, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "          )\n",
       "        )\n",
       "        (stochastic_depth): StochasticDepth(p=0.07500000000000001, mode=row)\n",
       "      )\n",
       "      (2): MBConv(\n",
       "        (block): Sequential(\n",
       "          (0): Conv2dNormActivation(\n",
       "            (0): Conv2d(80, 480, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(480, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (1): Conv2dNormActivation(\n",
       "            (0): Conv2d(480, 480, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=480, bias=False)\n",
       "            (1): BatchNorm2d(480, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (2): SqueezeExcitation(\n",
       "            (avgpool): AdaptiveAvgPool2d(output_size=1)\n",
       "            (fc1): Conv2d(480, 20, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (fc2): Conv2d(20, 480, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (activation): SiLU(inplace=True)\n",
       "            (scale_activation): Sigmoid()\n",
       "          )\n",
       "          (3): Conv2dNormActivation(\n",
       "            (0): Conv2d(480, 80, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(80, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "          )\n",
       "        )\n",
       "        (stochastic_depth): StochasticDepth(p=0.08750000000000001, mode=row)\n",
       "      )\n",
       "    )\n",
       "    (5): Sequential(\n",
       "      (0): MBConv(\n",
       "        (block): Sequential(\n",
       "          (0): Conv2dNormActivation(\n",
       "            (0): Conv2d(80, 480, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(480, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (1): Conv2dNormActivation(\n",
       "            (0): Conv2d(480, 480, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2), groups=480, bias=False)\n",
       "            (1): BatchNorm2d(480, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (2): SqueezeExcitation(\n",
       "            (avgpool): AdaptiveAvgPool2d(output_size=1)\n",
       "            (fc1): Conv2d(480, 20, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (fc2): Conv2d(20, 480, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (activation): SiLU(inplace=True)\n",
       "            (scale_activation): Sigmoid()\n",
       "          )\n",
       "          (3): Conv2dNormActivation(\n",
       "            (0): Conv2d(480, 112, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(112, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "          )\n",
       "        )\n",
       "        (stochastic_depth): StochasticDepth(p=0.1, mode=row)\n",
       "      )\n",
       "      (1): MBConv(\n",
       "        (block): Sequential(\n",
       "          (0): Conv2dNormActivation(\n",
       "            (0): Conv2d(112, 672, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(672, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (1): Conv2dNormActivation(\n",
       "            (0): Conv2d(672, 672, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2), groups=672, bias=False)\n",
       "            (1): BatchNorm2d(672, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (2): SqueezeExcitation(\n",
       "            (avgpool): AdaptiveAvgPool2d(output_size=1)\n",
       "            (fc1): Conv2d(672, 28, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (fc2): Conv2d(28, 672, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (activation): SiLU(inplace=True)\n",
       "            (scale_activation): Sigmoid()\n",
       "          )\n",
       "          (3): Conv2dNormActivation(\n",
       "            (0): Conv2d(672, 112, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(112, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "          )\n",
       "        )\n",
       "        (stochastic_depth): StochasticDepth(p=0.1125, mode=row)\n",
       "      )\n",
       "      (2): MBConv(\n",
       "        (block): Sequential(\n",
       "          (0): Conv2dNormActivation(\n",
       "            (0): Conv2d(112, 672, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(672, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (1): Conv2dNormActivation(\n",
       "            (0): Conv2d(672, 672, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2), groups=672, bias=False)\n",
       "            (1): BatchNorm2d(672, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (2): SqueezeExcitation(\n",
       "            (avgpool): AdaptiveAvgPool2d(output_size=1)\n",
       "            (fc1): Conv2d(672, 28, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (fc2): Conv2d(28, 672, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (activation): SiLU(inplace=True)\n",
       "            (scale_activation): Sigmoid()\n",
       "          )\n",
       "          (3): Conv2dNormActivation(\n",
       "            (0): Conv2d(672, 112, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(112, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "          )\n",
       "        )\n",
       "        (stochastic_depth): StochasticDepth(p=0.125, mode=row)\n",
       "      )\n",
       "    )\n",
       "    (6): Sequential(\n",
       "      (0): MBConv(\n",
       "        (block): Sequential(\n",
       "          (0): Conv2dNormActivation(\n",
       "            (0): Conv2d(112, 672, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(672, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (1): Conv2dNormActivation(\n",
       "            (0): Conv2d(672, 672, kernel_size=(5, 5), stride=(2, 2), padding=(2, 2), groups=672, bias=False)\n",
       "            (1): BatchNorm2d(672, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (2): SqueezeExcitation(\n",
       "            (avgpool): AdaptiveAvgPool2d(output_size=1)\n",
       "            (fc1): Conv2d(672, 28, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (fc2): Conv2d(28, 672, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (activation): SiLU(inplace=True)\n",
       "            (scale_activation): Sigmoid()\n",
       "          )\n",
       "          (3): Conv2dNormActivation(\n",
       "            (0): Conv2d(672, 192, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(192, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "          )\n",
       "        )\n",
       "        (stochastic_depth): StochasticDepth(p=0.1375, mode=row)\n",
       "      )\n",
       "      (1): MBConv(\n",
       "        (block): Sequential(\n",
       "          (0): Conv2dNormActivation(\n",
       "            (0): Conv2d(192, 1152, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(1152, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (1): Conv2dNormActivation(\n",
       "            (0): Conv2d(1152, 1152, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2), groups=1152, bias=False)\n",
       "            (1): BatchNorm2d(1152, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (2): SqueezeExcitation(\n",
       "            (avgpool): AdaptiveAvgPool2d(output_size=1)\n",
       "            (fc1): Conv2d(1152, 48, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (fc2): Conv2d(48, 1152, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (activation): SiLU(inplace=True)\n",
       "            (scale_activation): Sigmoid()\n",
       "          )\n",
       "          (3): Conv2dNormActivation(\n",
       "            (0): Conv2d(1152, 192, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(192, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "          )\n",
       "        )\n",
       "        (stochastic_depth): StochasticDepth(p=0.15000000000000002, mode=row)\n",
       "      )\n",
       "      (2): MBConv(\n",
       "        (block): Sequential(\n",
       "          (0): Conv2dNormActivation(\n",
       "            (0): Conv2d(192, 1152, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(1152, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (1): Conv2dNormActivation(\n",
       "            (0): Conv2d(1152, 1152, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2), groups=1152, bias=False)\n",
       "            (1): BatchNorm2d(1152, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (2): SqueezeExcitation(\n",
       "            (avgpool): AdaptiveAvgPool2d(output_size=1)\n",
       "            (fc1): Conv2d(1152, 48, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (fc2): Conv2d(48, 1152, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (activation): SiLU(inplace=True)\n",
       "            (scale_activation): Sigmoid()\n",
       "          )\n",
       "          (3): Conv2dNormActivation(\n",
       "            (0): Conv2d(1152, 192, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(192, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "          )\n",
       "        )\n",
       "        (stochastic_depth): StochasticDepth(p=0.1625, mode=row)\n",
       "      )\n",
       "      (3): MBConv(\n",
       "        (block): Sequential(\n",
       "          (0): Conv2dNormActivation(\n",
       "            (0): Conv2d(192, 1152, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(1152, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (1): Conv2dNormActivation(\n",
       "            (0): Conv2d(1152, 1152, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2), groups=1152, bias=False)\n",
       "            (1): BatchNorm2d(1152, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (2): SqueezeExcitation(\n",
       "            (avgpool): AdaptiveAvgPool2d(output_size=1)\n",
       "            (fc1): Conv2d(1152, 48, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (fc2): Conv2d(48, 1152, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (activation): SiLU(inplace=True)\n",
       "            (scale_activation): Sigmoid()\n",
       "          )\n",
       "          (3): Conv2dNormActivation(\n",
       "            (0): Conv2d(1152, 192, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(192, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "          )\n",
       "        )\n",
       "        (stochastic_depth): StochasticDepth(p=0.17500000000000002, mode=row)\n",
       "      )\n",
       "    )\n",
       "    (7): Sequential(\n",
       "      (0): MBConv(\n",
       "        (block): Sequential(\n",
       "          (0): Conv2dNormActivation(\n",
       "            (0): Conv2d(192, 1152, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(1152, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (1): Conv2dNormActivation(\n",
       "            (0): Conv2d(1152, 1152, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=1152, bias=False)\n",
       "            (1): BatchNorm2d(1152, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "            (2): SiLU(inplace=True)\n",
       "          )\n",
       "          (2): SqueezeExcitation(\n",
       "            (avgpool): AdaptiveAvgPool2d(output_size=1)\n",
       "            (fc1): Conv2d(1152, 48, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (fc2): Conv2d(48, 1152, kernel_size=(1, 1), stride=(1, 1))\n",
       "            (activation): SiLU(inplace=True)\n",
       "            (scale_activation): Sigmoid()\n",
       "          )\n",
       "          (3): Conv2dNormActivation(\n",
       "            (0): Conv2d(1152, 320, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "            (1): BatchNorm2d(320, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "          )\n",
       "        )\n",
       "        (stochastic_depth): StochasticDepth(p=0.1875, mode=row)\n",
       "      )\n",
       "    )\n",
       "    (8): Conv2dNormActivation(\n",
       "      (0): Conv2d(320, 1280, kernel_size=(1, 1), stride=(1, 1), bias=False)\n",
       "      (1): BatchNorm2d(1280, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)\n",
       "      (2): SiLU(inplace=True)\n",
       "    )\n",
       "  )\n",
       "  (avgpool): AdaptiveAvgPool2d(output_size=1)\n",
       "  (classifier): Sequential(\n",
       "    (0): Dropout(p=0.2, inplace=True)\n",
       "    (1): Linear(in_features=1280, out_features=1000, bias=True)\n",
       "  )\n",
       ")"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model = torchvision.models.efficientnet_b0(weights=weights).to(device)\n",
    "model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "f1b7082d",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:04:27.557567Z",
     "iopub.status.busy": "2024-08-25T16:04:27.557120Z",
     "iopub.status.idle": "2024-08-25T16:04:37.907590Z",
     "shell.execute_reply": "2024-08-25T16:04:37.906316Z"
    },
    "papermill": {
     "duration": 10.384344,
     "end_time": "2024-08-25T16:04:37.910256",
     "exception": false,
     "start_time": "2024-08-25T16:04:27.525912",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "============================================================================================================================================\n",
       "Layer (type (var_name))                                      Input Shape          Output Shape         Param #              Trainable\n",
       "============================================================================================================================================\n",
       "EfficientNet (EfficientNet)                                  [32, 3, 224, 224]    [32, 1000]           --                   True\n",
       "├─Sequential (features)                                      [32, 3, 224, 224]    [32, 2304, 7, 7]     --                   True\n",
       "│    └─Conv2dNormActivation (0)                              [32, 3, 224, 224]    [32, 56, 112, 112]   --                   True\n",
       "│    │    └─Conv2d (0)                                       [32, 3, 224, 224]    [32, 56, 112, 112]   1,512                True\n",
       "│    │    └─BatchNorm2d (1)                                  [32, 56, 112, 112]   [32, 56, 112, 112]   112                  True\n",
       "│    │    └─SiLU (2)                                         [32, 56, 112, 112]   [32, 56, 112, 112]   --                   --\n",
       "│    └─Sequential (1)                                        [32, 56, 112, 112]   [32, 32, 112, 112]   --                   True\n",
       "│    │    └─MBConv (0)                                       [32, 56, 112, 112]   [32, 32, 112, 112]   4,110                True\n",
       "│    │    └─MBConv (1)                                       [32, 32, 112, 112]   [32, 32, 112, 112]   1,992                True\n",
       "│    │    └─MBConv (2)                                       [32, 32, 112, 112]   [32, 32, 112, 112]   1,992                True\n",
       "│    └─Sequential (2)                                        [32, 32, 112, 112]   [32, 40, 56, 56]     --                   True\n",
       "│    │    └─MBConv (0)                                       [32, 32, 112, 112]   [32, 40, 56, 56]     19,672               True\n",
       "│    │    └─MBConv (1)                                       [32, 40, 56, 56]     [32, 40, 56, 56]     27,450               True\n",
       "│    │    └─MBConv (2)                                       [32, 40, 56, 56]     [32, 40, 56, 56]     27,450               True\n",
       "│    │    └─MBConv (3)                                       [32, 40, 56, 56]     [32, 40, 56, 56]     27,450               True\n",
       "│    │    └─MBConv (4)                                       [32, 40, 56, 56]     [32, 40, 56, 56]     27,450               True\n",
       "│    │    └─MBConv (5)                                       [32, 40, 56, 56]     [32, 40, 56, 56]     27,450               True\n",
       "│    └─Sequential (3)                                        [32, 40, 56, 56]     [32, 72, 28, 28]     --                   True\n",
       "│    │    └─MBConv (0)                                       [32, 40, 56, 56]     [32, 72, 28, 28]     39,034               True\n",
       "│    │    └─MBConv (1)                                       [32, 72, 28, 28]     [32, 72, 28, 28]     90,882               True\n",
       "│    │    └─MBConv (2)                                       [32, 72, 28, 28]     [32, 72, 28, 28]     90,882               True\n",
       "│    │    └─MBConv (3)                                       [32, 72, 28, 28]     [32, 72, 28, 28]     90,882               True\n",
       "│    │    └─MBConv (4)                                       [32, 72, 28, 28]     [32, 72, 28, 28]     90,882               True\n",
       "│    │    └─MBConv (5)                                       [32, 72, 28, 28]     [32, 72, 28, 28]     90,882               True\n",
       "│    └─Sequential (4)                                        [32, 72, 28, 28]     [32, 144, 14, 14]    --                   True\n",
       "│    │    └─MBConv (0)                                       [32, 72, 28, 28]     [32, 144, 14, 14]    115,218              True\n",
       "│    │    └─MBConv (1)                                       [32, 144, 14, 14]    [32, 144, 14, 14]    323,460              True\n",
       "│    │    └─MBConv (2)                                       [32, 144, 14, 14]    [32, 144, 14, 14]    323,460              True\n",
       "│    │    └─MBConv (3)                                       [32, 144, 14, 14]    [32, 144, 14, 14]    323,460              True\n",
       "│    │    └─MBConv (4)                                       [32, 144, 14, 14]    [32, 144, 14, 14]    323,460              True\n",
       "│    │    └─MBConv (5)                                       [32, 144, 14, 14]    [32, 144, 14, 14]    323,460              True\n",
       "│    │    └─MBConv (6)                                       [32, 144, 14, 14]    [32, 144, 14, 14]    323,460              True\n",
       "│    │    └─MBConv (7)                                       [32, 144, 14, 14]    [32, 144, 14, 14]    323,460              True\n",
       "│    └─Sequential (5)                                        [32, 144, 14, 14]    [32, 200, 14, 14]    --                   True\n",
       "│    │    └─MBConv (0)                                       [32, 144, 14, 14]    [32, 200, 14, 14]    385,780              True\n",
       "│    │    └─MBConv (1)                                       [32, 200, 14, 14]    [32, 200, 14, 14]    636,450              True\n",
       "│    │    └─MBConv (2)                                       [32, 200, 14, 14]    [32, 200, 14, 14]    636,450              True\n",
       "│    │    └─MBConv (3)                                       [32, 200, 14, 14]    [32, 200, 14, 14]    636,450              True\n",
       "│    │    └─MBConv (4)                                       [32, 200, 14, 14]    [32, 200, 14, 14]    636,450              True\n",
       "│    │    └─MBConv (5)                                       [32, 200, 14, 14]    [32, 200, 14, 14]    636,450              True\n",
       "│    │    └─MBConv (6)                                       [32, 200, 14, 14]    [32, 200, 14, 14]    636,450              True\n",
       "│    │    └─MBConv (7)                                       [32, 200, 14, 14]    [32, 200, 14, 14]    636,450              True\n",
       "│    └─Sequential (6)                                        [32, 200, 14, 14]    [32, 344, 7, 7]      --                   True\n",
       "│    │    └─MBConv (0)                                       [32, 200, 14, 14]    [32, 344, 7, 7]      809,538              True\n",
       "│    │    └─MBConv (1)                                       [32, 344, 7, 7]      [32, 344, 7, 7]      1,837,734            True\n",
       "│    │    └─MBConv (2)                                       [32, 344, 7, 7]      [32, 344, 7, 7]      1,837,734            True\n",
       "│    │    └─MBConv (3)                                       [32, 344, 7, 7]      [32, 344, 7, 7]      1,837,734            True\n",
       "│    │    └─MBConv (4)                                       [32, 344, 7, 7]      [32, 344, 7, 7]      1,837,734            True\n",
       "│    │    └─MBConv (5)                                       [32, 344, 7, 7]      [32, 344, 7, 7]      1,837,734            True\n",
       "│    │    └─MBConv (6)                                       [32, 344, 7, 7]      [32, 344, 7, 7]      1,837,734            True\n",
       "│    │    └─MBConv (7)                                       [32, 344, 7, 7]      [32, 344, 7, 7]      1,837,734            True\n",
       "│    │    └─MBConv (8)                                       [32, 344, 7, 7]      [32, 344, 7, 7]      1,837,734            True\n",
       "│    │    └─MBConv (9)                                       [32, 344, 7, 7]      [32, 344, 7, 7]      1,837,734            True\n",
       "│    │    └─MBConv (10)                                      [32, 344, 7, 7]      [32, 344, 7, 7]      1,837,734            True\n",
       "│    └─Sequential (7)                                        [32, 344, 7, 7]      [32, 576, 7, 7]      --                   True\n",
       "│    │    └─MBConv (0)                                       [32, 344, 7, 7]      [32, 576, 7, 7]      2,284,022            True\n",
       "│    │    └─MBConv (1)                                       [32, 576, 7, 7]      [32, 576, 7, 7]      5,026,320            True\n",
       "│    │    └─MBConv (2)                                       [32, 576, 7, 7]      [32, 576, 7, 7]      5,026,320            True\n",
       "│    └─Conv2dNormActivation (8)                              [32, 576, 7, 7]      [32, 2304, 7, 7]     --                   True\n",
       "│    │    └─Conv2d (0)                                       [32, 576, 7, 7]      [32, 2304, 7, 7]     1,327,104            True\n",
       "│    │    └─BatchNorm2d (1)                                  [32, 2304, 7, 7]     [32, 2304, 7, 7]     4,608                True\n",
       "│    │    └─SiLU (2)                                         [32, 2304, 7, 7]     [32, 2304, 7, 7]     --                   --\n",
       "├─AdaptiveAvgPool2d (avgpool)                                [32, 2304, 7, 7]     [32, 2304, 1, 1]     --                   --\n",
       "├─Sequential (classifier)                                    [32, 2304]           [32, 1000]           --                   True\n",
       "│    └─Dropout (0)                                           [32, 2304]           [32, 2304]           --                   --\n",
       "│    └─Linear (1)                                            [32, 2304]           [32, 1000]           2,305,000            True\n",
       "============================================================================================================================================\n",
       "Total params: 43,040,704\n",
       "Trainable params: 43,040,704\n",
       "Non-trainable params: 0\n",
       "Total mult-adds (G): 107.53\n",
       "============================================================================================================================================\n",
       "Input size (MB): 19.27\n",
       "Forward/backward pass size (MB): 15328.84\n",
       "Params size (MB): 172.16\n",
       "Estimated Total Size (MB): 15520.27\n",
       "============================================================================================================================================"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "summary(model=model_6, \n",
    "        input_size=(32, 3, 224, 224), # make sure this is \"input_size\", not \"input_shape\"\n",
    "        # col_names=[\"input_size\"], # uncomment for smaller output\n",
    "        col_names=[\"input_size\", \"output_size\", \"num_params\", \"trainable\"],\n",
    "        col_width=20,\n",
    "        row_settings=[\"var_names\"]\n",
    ") "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "58a2c7b4",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:04:37.969207Z",
     "iopub.status.busy": "2024-08-25T16:04:37.968722Z",
     "iopub.status.idle": "2024-08-25T16:04:39.719960Z",
     "shell.execute_reply": "2024-08-25T16:04:39.718688Z"
    },
    "papermill": {
     "duration": 1.783894,
     "end_time": "2024-08-25T16:04:39.723438",
     "exception": false,
     "start_time": "2024-08-25T16:04:37.939544",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "============================================================================================================================================\n",
       "Layer (type (var_name))                                      Input Shape          Output Shape         Param #              Trainable\n",
       "============================================================================================================================================\n",
       "EfficientNet (EfficientNet)                                  [32, 3, 224, 224]    [32, 1000]           --                   True\n",
       "├─Sequential (features)                                      [32, 3, 224, 224]    [32, 1280, 7, 7]     --                   True\n",
       "│    └─Conv2dNormActivation (0)                              [32, 3, 224, 224]    [32, 32, 112, 112]   --                   True\n",
       "│    │    └─Conv2d (0)                                       [32, 3, 224, 224]    [32, 32, 112, 112]   864                  True\n",
       "│    │    └─BatchNorm2d (1)                                  [32, 32, 112, 112]   [32, 32, 112, 112]   64                   True\n",
       "│    │    └─SiLU (2)                                         [32, 32, 112, 112]   [32, 32, 112, 112]   --                   --\n",
       "│    └─Sequential (1)                                        [32, 32, 112, 112]   [32, 16, 112, 112]   --                   True\n",
       "│    │    └─MBConv (0)                                       [32, 32, 112, 112]   [32, 16, 112, 112]   1,448                True\n",
       "│    └─Sequential (2)                                        [32, 16, 112, 112]   [32, 24, 56, 56]     --                   True\n",
       "│    │    └─MBConv (0)                                       [32, 16, 112, 112]   [32, 24, 56, 56]     6,004                True\n",
       "│    │    └─MBConv (1)                                       [32, 24, 56, 56]     [32, 24, 56, 56]     10,710               True\n",
       "│    └─Sequential (3)                                        [32, 24, 56, 56]     [32, 40, 28, 28]     --                   True\n",
       "│    │    └─MBConv (0)                                       [32, 24, 56, 56]     [32, 40, 28, 28]     15,350               True\n",
       "│    │    └─MBConv (1)                                       [32, 40, 28, 28]     [32, 40, 28, 28]     31,290               True\n",
       "│    └─Sequential (4)                                        [32, 40, 28, 28]     [32, 80, 14, 14]     --                   True\n",
       "│    │    └─MBConv (0)                                       [32, 40, 28, 28]     [32, 80, 14, 14]     37,130               True\n",
       "│    │    └─MBConv (1)                                       [32, 80, 14, 14]     [32, 80, 14, 14]     102,900              True\n",
       "│    │    └─MBConv (2)                                       [32, 80, 14, 14]     [32, 80, 14, 14]     102,900              True\n",
       "│    └─Sequential (5)                                        [32, 80, 14, 14]     [32, 112, 14, 14]    --                   True\n",
       "│    │    └─MBConv (0)                                       [32, 80, 14, 14]     [32, 112, 14, 14]    126,004              True\n",
       "│    │    └─MBConv (1)                                       [32, 112, 14, 14]    [32, 112, 14, 14]    208,572              True\n",
       "│    │    └─MBConv (2)                                       [32, 112, 14, 14]    [32, 112, 14, 14]    208,572              True\n",
       "│    └─Sequential (6)                                        [32, 112, 14, 14]    [32, 192, 7, 7]      --                   True\n",
       "│    │    └─MBConv (0)                                       [32, 112, 14, 14]    [32, 192, 7, 7]      262,492              True\n",
       "│    │    └─MBConv (1)                                       [32, 192, 7, 7]      [32, 192, 7, 7]      587,952              True\n",
       "│    │    └─MBConv (2)                                       [32, 192, 7, 7]      [32, 192, 7, 7]      587,952              True\n",
       "│    │    └─MBConv (3)                                       [32, 192, 7, 7]      [32, 192, 7, 7]      587,952              True\n",
       "│    └─Sequential (7)                                        [32, 192, 7, 7]      [32, 320, 7, 7]      --                   True\n",
       "│    │    └─MBConv (0)                                       [32, 192, 7, 7]      [32, 320, 7, 7]      717,232              True\n",
       "│    └─Conv2dNormActivation (8)                              [32, 320, 7, 7]      [32, 1280, 7, 7]     --                   True\n",
       "│    │    └─Conv2d (0)                                       [32, 320, 7, 7]      [32, 1280, 7, 7]     409,600              True\n",
       "│    │    └─BatchNorm2d (1)                                  [32, 1280, 7, 7]     [32, 1280, 7, 7]     2,560                True\n",
       "│    │    └─SiLU (2)                                         [32, 1280, 7, 7]     [32, 1280, 7, 7]     --                   --\n",
       "├─AdaptiveAvgPool2d (avgpool)                                [32, 1280, 7, 7]     [32, 1280, 1, 1]     --                   --\n",
       "├─Sequential (classifier)                                    [32, 1280]           [32, 1000]           --                   True\n",
       "│    └─Dropout (0)                                           [32, 1280]           [32, 1280]           --                   --\n",
       "│    └─Linear (1)                                            [32, 1280]           [32, 1000]           1,281,000            True\n",
       "============================================================================================================================================\n",
       "Total params: 5,288,548\n",
       "Trainable params: 5,288,548\n",
       "Non-trainable params: 0\n",
       "Total mult-adds (G): 12.35\n",
       "============================================================================================================================================\n",
       "Input size (MB): 19.27\n",
       "Forward/backward pass size (MB): 3452.35\n",
       "Params size (MB): 21.15\n",
       "Estimated Total Size (MB): 3492.77\n",
       "============================================================================================================================================"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from torchinfo import summary\n",
    "summary(model=model,input_size=(32,3,224,224),\n",
    "               col_names=[\"input_size\", \"output_size\", \"num_params\",\"trainable\"],\n",
    "               col_width=20,\n",
    "                row_settings=[\"var_names\"])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "9cb67b7c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:04:39.786187Z",
     "iopub.status.busy": "2024-08-25T16:04:39.785692Z",
     "iopub.status.idle": "2024-08-25T16:04:39.793451Z",
     "shell.execute_reply": "2024-08-25T16:04:39.792028Z"
    },
    "papermill": {
     "duration": 0.041894,
     "end_time": "2024-08-25T16:04:39.796135",
     "exception": false,
     "start_time": "2024-08-25T16:04:39.754241",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "for params in model.features.parameters():\n",
    "    params.requires_grad=False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "b9bfae0f",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:04:39.853871Z",
     "iopub.status.busy": "2024-08-25T16:04:39.853419Z",
     "iopub.status.idle": "2024-08-25T16:04:39.870661Z",
     "shell.execute_reply": "2024-08-25T16:04:39.869105Z"
    },
    "papermill": {
     "duration": 0.049941,
     "end_time": "2024-08-25T16:04:39.874304",
     "exception": false,
     "start_time": "2024-08-25T16:04:39.824363",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from torch import nn\n",
    "torch.manual_seed(42)\n",
    "torch.cuda.manual_seed(42)\n",
    "\n",
    "outshape=len(class_name)\n",
    "model.classifier=torch.nn.Sequential(nn.Dropout(p=0.2, inplace=True),\n",
    "                                     nn.Linear(in_features=1280, out_features=outshape, bias=True)).to(device)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "573d2dd8",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:04:39.935081Z",
     "iopub.status.busy": "2024-08-25T16:04:39.934637Z",
     "iopub.status.idle": "2024-08-25T16:04:41.671625Z",
     "shell.execute_reply": "2024-08-25T16:04:41.670448Z"
    },
    "papermill": {
     "duration": 1.770585,
     "end_time": "2024-08-25T16:04:41.674200",
     "exception": false,
     "start_time": "2024-08-25T16:04:39.903615",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "============================================================================================================================================\n",
       "Layer (type (var_name))                                      Input Shape          Output Shape         Param #              Trainable\n",
       "============================================================================================================================================\n",
       "EfficientNet (EfficientNet)                                  [32, 3, 224, 224]    [32, 3]              --                   Partial\n",
       "├─Sequential (features)                                      [32, 3, 224, 224]    [32, 1280, 7, 7]     --                   False\n",
       "│    └─Conv2dNormActivation (0)                              [32, 3, 224, 224]    [32, 32, 112, 112]   --                   False\n",
       "│    │    └─Conv2d (0)                                       [32, 3, 224, 224]    [32, 32, 112, 112]   (864)                False\n",
       "│    │    └─BatchNorm2d (1)                                  [32, 32, 112, 112]   [32, 32, 112, 112]   (64)                 False\n",
       "│    │    └─SiLU (2)                                         [32, 32, 112, 112]   [32, 32, 112, 112]   --                   --\n",
       "│    └─Sequential (1)                                        [32, 32, 112, 112]   [32, 16, 112, 112]   --                   False\n",
       "│    │    └─MBConv (0)                                       [32, 32, 112, 112]   [32, 16, 112, 112]   (1,448)              False\n",
       "│    └─Sequential (2)                                        [32, 16, 112, 112]   [32, 24, 56, 56]     --                   False\n",
       "│    │    └─MBConv (0)                                       [32, 16, 112, 112]   [32, 24, 56, 56]     (6,004)              False\n",
       "│    │    └─MBConv (1)                                       [32, 24, 56, 56]     [32, 24, 56, 56]     (10,710)             False\n",
       "│    └─Sequential (3)                                        [32, 24, 56, 56]     [32, 40, 28, 28]     --                   False\n",
       "│    │    └─MBConv (0)                                       [32, 24, 56, 56]     [32, 40, 28, 28]     (15,350)             False\n",
       "│    │    └─MBConv (1)                                       [32, 40, 28, 28]     [32, 40, 28, 28]     (31,290)             False\n",
       "│    └─Sequential (4)                                        [32, 40, 28, 28]     [32, 80, 14, 14]     --                   False\n",
       "│    │    └─MBConv (0)                                       [32, 40, 28, 28]     [32, 80, 14, 14]     (37,130)             False\n",
       "│    │    └─MBConv (1)                                       [32, 80, 14, 14]     [32, 80, 14, 14]     (102,900)            False\n",
       "│    │    └─MBConv (2)                                       [32, 80, 14, 14]     [32, 80, 14, 14]     (102,900)            False\n",
       "│    └─Sequential (5)                                        [32, 80, 14, 14]     [32, 112, 14, 14]    --                   False\n",
       "│    │    └─MBConv (0)                                       [32, 80, 14, 14]     [32, 112, 14, 14]    (126,004)            False\n",
       "│    │    └─MBConv (1)                                       [32, 112, 14, 14]    [32, 112, 14, 14]    (208,572)            False\n",
       "│    │    └─MBConv (2)                                       [32, 112, 14, 14]    [32, 112, 14, 14]    (208,572)            False\n",
       "│    └─Sequential (6)                                        [32, 112, 14, 14]    [32, 192, 7, 7]      --                   False\n",
       "│    │    └─MBConv (0)                                       [32, 112, 14, 14]    [32, 192, 7, 7]      (262,492)            False\n",
       "│    │    └─MBConv (1)                                       [32, 192, 7, 7]      [32, 192, 7, 7]      (587,952)            False\n",
       "│    │    └─MBConv (2)                                       [32, 192, 7, 7]      [32, 192, 7, 7]      (587,952)            False\n",
       "│    │    └─MBConv (3)                                       [32, 192, 7, 7]      [32, 192, 7, 7]      (587,952)            False\n",
       "│    └─Sequential (7)                                        [32, 192, 7, 7]      [32, 320, 7, 7]      --                   False\n",
       "│    │    └─MBConv (0)                                       [32, 192, 7, 7]      [32, 320, 7, 7]      (717,232)            False\n",
       "│    └─Conv2dNormActivation (8)                              [32, 320, 7, 7]      [32, 1280, 7, 7]     --                   False\n",
       "│    │    └─Conv2d (0)                                       [32, 320, 7, 7]      [32, 1280, 7, 7]     (409,600)            False\n",
       "│    │    └─BatchNorm2d (1)                                  [32, 1280, 7, 7]     [32, 1280, 7, 7]     (2,560)              False\n",
       "│    │    └─SiLU (2)                                         [32, 1280, 7, 7]     [32, 1280, 7, 7]     --                   --\n",
       "├─AdaptiveAvgPool2d (avgpool)                                [32, 1280, 7, 7]     [32, 1280, 1, 1]     --                   --\n",
       "├─Sequential (classifier)                                    [32, 1280]           [32, 3]              --                   True\n",
       "│    └─Dropout (0)                                           [32, 1280]           [32, 1280]           --                   --\n",
       "│    └─Linear (1)                                            [32, 1280]           [32, 3]              3,843                True\n",
       "============================================================================================================================================\n",
       "Total params: 4,011,391\n",
       "Trainable params: 3,843\n",
       "Non-trainable params: 4,007,548\n",
       "Total mult-adds (G): 12.31\n",
       "============================================================================================================================================\n",
       "Input size (MB): 19.27\n",
       "Forward/backward pass size (MB): 3452.09\n",
       "Params size (MB): 16.05\n",
       "Estimated Total Size (MB): 3487.41\n",
       "============================================================================================================================================"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "summary(model=model,input_size=(32,3,224,224),\n",
    "               col_names=[\"input_size\", \"output_size\", \"num_params\",\"trainable\"],\n",
    "               col_width=20,\n",
    "                row_settings=[\"var_names\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "d64bf9c8",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:04:41.732681Z",
     "iopub.status.busy": "2024-08-25T16:04:41.732238Z",
     "iopub.status.idle": "2024-08-25T16:04:41.740202Z",
     "shell.execute_reply": "2024-08-25T16:04:41.739007Z"
    },
    "papermill": {
     "duration": 0.04036,
     "end_time": "2024-08-25T16:04:41.742637",
     "exception": false,
     "start_time": "2024-08-25T16:04:41.702277",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "loss_fn=nn.CrossEntropyLoss()\n",
    "optimizer=torch.optim.Adam(params=model.parameters(),lr=0.001)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "55c2c643",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:04:41.800678Z",
     "iopub.status.busy": "2024-08-25T16:04:41.800228Z",
     "iopub.status.idle": "2024-08-25T16:06:17.153852Z",
     "shell.execute_reply": "2024-08-25T16:06:17.151873Z"
    },
    "papermill": {
     "duration": 95.387315,
     "end_time": "2024-08-25T16:06:17.158159",
     "exception": false,
     "start_time": "2024-08-25T16:04:41.770844",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "906e09f0a4e04938a00ba725d25db39d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "  0%|          | 0/5 [00:00<?, ?it/s]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch: 1 | train_loss: 1.0438 | train_acc: 0.4102 | test_loss: 0.8607 | test_acc: 0.6515\n",
      "Epoch: 2 | train_loss: 0.9343 | train_acc: 0.6133 | test_loss: 0.7065 | test_acc: 0.8655\n",
      "Epoch: 3 | train_loss: 0.7661 | train_acc: 0.7617 | test_loss: 0.7064 | test_acc: 0.8049\n",
      "Epoch: 4 | train_loss: 0.6662 | train_acc: 0.8945 | test_loss: 0.6753 | test_acc: 0.8258\n",
      "Epoch: 5 | train_loss: 0.6829 | train_acc: 0.7227 | test_loss: 0.6340 | test_acc: 0.8059\n",
      "95.34435583800007\n"
     ]
    }
   ],
   "source": [
    "from timeit import default_timer as timer\n",
    "\n",
    "start_time=timer()\n",
    "model_result=engine.train(model=model,\n",
    "                       train_dataloader=train_dataloader,\n",
    "                       test_dataloader=test_dataloader,\n",
    "                       optimizer=optimizer,\n",
    "                       loss_fn=loss_fn,\n",
    "                       epochs=5,\n",
    "                       device=device)\n",
    "end_time=timer()\n",
    "print(end_time-start_time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "86c91fbe",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-08-25T16:06:17.223003Z",
     "iopub.status.busy": "2024-08-25T16:06:17.221681Z",
     "iopub.status.idle": "2024-08-25T16:06:18.117847Z",
     "shell.execute_reply": "2024-08-25T16:06:18.116302Z"
    },
    "papermill": {
     "duration": 0.932238,
     "end_time": "2024-08-25T16:06:18.121284",
     "exception": false,
     "start_time": "2024-08-25T16:06:17.189046",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[INFO] Couldn't find helper_functions.py, downloading...\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABL4AAAJwCAYAAACH0KjyAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuNSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/xnp5ZAAAACXBIWXMAAA9hAAAPYQGoP6dpAADdtklEQVR4nOzdd3QU5dvG8e9ueg+BEDqhd0JvCqKAKIICKoiFJioovipWlI6KPwsWRLHQBQUFFEWQohQBCS30GgKhBkJJSE925/1jMRoISCDJbJLrc86eDLOzO9dmM2H2zvPcYzEMw0BERERERERERKSQsZodQEREREREREREJC+o8CUiIiIiIiIiIoWSCl8iIiIiIiIiIlIoqfAlIiIiIiIiIiKFkgpfIiIiIiIiIiJSKKnwJSIiIiIiIiIihZIKXyIiIiIiIiIiUiip8CUiIiIiIiIiIoWSCl8iIiIiIiIiIlIoqfAlIiIiIiIiIiKFkgpfImKqadOmYbFY2LRpk9lRREREROSSzz77DIvFQvPmzc2OIiJyU1T4EhERERERkSxmzZpFaGgo4eHhHDx40Ow4IiI3TIUvERERERERyRQVFcW6desYP348wcHBzJo1y+xI2UpMTDQ7gogUACp8iYjT27p1K3fffTf+/v74+vrSrl07/vrrryzbpKenM3r0aKpVq4anpyfFixfn1ltvZdmyZZnbnDp1in79+lGuXDk8PDwoXbo09913H4cPH87nVyQiIiLivGbNmkWxYsW45557eOCBB7ItfF24cIEXXniB0NBQPDw8KFeuHL179yY2NjZzm5SUFEaNGkX16tXx9PSkdOnSdO/encjISABWrlyJxWJh5cqVWZ778OHDWCwWpk2blrmub9+++Pr6EhkZSadOnfDz8+ORRx4BYM2aNTz44INUqFABDw8PypcvzwsvvEBycvIVuffu3UuPHj0IDg7Gy8uLGjVq8MYbbwDwxx9/YLFYWLBgwRWPmz17NhaLhfXr1+f4+yki5nI1O4CIyLXs2rWL1q1b4+/vzyuvvIKbmxtffPEFbdu2ZdWqVZl9J0aNGsW4ceMYMGAAzZo1Iz4+nk2bNrFlyxY6dOgAwP3338+uXbt49tlnCQ0N5fTp0yxbtozo6GhCQ0NNfJUiIiIizmPWrFl0794dd3d3evXqxeeff87GjRtp2rQpAAkJCbRu3Zo9e/bQv39/GjVqRGxsLAsXLuTYsWOUKFECm81G586dWbFiBQ899BDPPfccFy9eZNmyZezcuZMqVarkOFdGRgYdO3bk1ltv5f3338fb2xuA77//nqSkJAYNGkTx4sUJDw9nwoQJHDt2jO+//z7z8du3b6d169a4ubnx5JNPEhoaSmRkJD///DNvvfUWbdu2pXz58syaNYtu3bpd8T2pUqUKLVu2vInvrIiYwhARMdHUqVMNwNi4cWO293ft2tVwd3c3IiMjM9edOHHC8PPzM9q0aZO5LiwszLjnnnuuup/z588bgPHee+/lXngRERGRQmbTpk0GYCxbtswwDMOw2+1GuXLljOeeey5zmxEjRhiAMX/+/Cseb7fbDcMwjClTphiAMX78+Ktu88cffxiA8ccff2S5PyoqygCMqVOnZq7r06ePARivvfbaFc+XlJR0xbpx48YZFovFOHLkSOa6Nm3aGH5+flnW/TuPYRjG0KFDDQ8PD+PChQuZ606fPm24uroaI0eOvGI/IuL8NNVRRJyWzWZj6dKldO3alcqVK2euL126NA8//DB//vkn8fHxAAQGBrJr1y4OHDiQ7XN5eXnh7u7OypUrOX/+fL7kFxERESloZs2aRUhICLfffjsAFouFnj178t1332Gz2QCYN28eYWFhV4yK+nv7v7cpUaIEzz777FW3uRGDBg26Yp2Xl1fmcmJiIrGxsbRq1QrDMNi6dSsAZ86cYfXq1fTv358KFSpcNU/v3r1JTU3lhx9+yFw3Z84cMjIyePTRR284t4iYR4UvEXFaZ86cISkpiRo1alxxX61atbDb7Rw9ehSAMWPGcOHCBapXr069evV4+eWX2b59e+b2Hh4e/O9//2Px4sWEhITQpk0b3n33XU6dOpVvr0dERETEmdlsNr777jtuv/12oqKiOHjwIAcPHqR58+bExMSwYsUKACIjI6lbt+41nysyMpIaNWrg6pp73XVcXV0pV67cFeujo6Pp27cvQUFB+Pr6EhwczG233QZAXFwcAIcOHQL4z9w1a9akadOmWfqazZo1ixYtWlC1atXceikiko9U+BKRQqFNmzZERkYyZcoU6taty9dff02jRo34+uuvM7d5/vnn2b9/P+PGjcPT05Phw4dTq1atzL8EioiIiBRlv//+OydPnuS7776jWrVqmbcePXoA5PrVHa828uvvkWWX8/DwwGq1XrFthw4dWLRoEa+++io//vgjy5Yty2yMb7fbc5yrd+/erFq1imPHjhEZGclff/2l0V4iBZia24uI0woODsbb25t9+/Zdcd/evXuxWq2UL18+c11QUBD9+vWjX79+JCQk0KZNG0aNGsWAAQMyt6lSpQovvvgiL774IgcOHKBBgwZ88MEHfPPNN/nymkRERESc1axZsyhZsiQTJ0684r758+ezYMECJk2aRJUqVdi5c+c1n6tKlSps2LCB9PR03Nzcst2mWLFigOMKkf925MiR6868Y8cO9u/fz/Tp0+ndu3fm+n9f2RvIbJvxX7kBHnroIYYMGcK3335LcnIybm5u9OzZ87oziYhz0YgvEXFaLi4u3Hnnnfz0008cPnw4c31MTAyzZ8/m1ltvxd/fH4CzZ89meayvry9Vq1YlNTUVgKSkJFJSUrJsU6VKFfz8/DK3ERERESmqkpOTmT9/Pp07d+aBBx644jZ48GAuXrzIwoULuf/++9m2bRsLFiy44nkMwwAcV9OOjY3l008/veo2FStWxMXFhdWrV2e5/7PPPrvu3C4uLlme8+/ljz/+OMt2wcHBtGnThilTphAdHZ1tnr+VKFGCu+++m2+++YZZs2Zx1113UaJEievOJCLORSO+RMQpTJkyhSVLllyxftSoUSxbtoxbb72Vp59+GldXV7744gtSU1N59913M7erXbs2bdu2pXHjxgQFBbFp0yZ++OEHBg8eDMD+/ftp164dPXr0oHbt2ri6urJgwQJiYmJ46KGH8u11ioiIiDijhQsXcvHiRe69995s72/RogXBwcHMmjWL2bNn88MPP/Dggw/Sv39/GjduzLlz51i4cCGTJk0iLCyM3r17M2PGDIYMGUJ4eDitW7cmMTGR5cuX8/TTT3PfffcREBDAgw8+yIQJE7BYLFSpUoVffvmF06dPX3fumjVrUqVKFV566SWOHz+Ov78/8+bNy/ZiRp988gm33norjRo14sknn6RSpUocPnyYRYsWERERkWXb3r1788ADDwAwduzY6/9GiojzMfOSkiIiU6dONYCr3o4ePWps2bLF6Nixo+Hr62t4e3sbt99+u7Fu3bosz/Pmm28azZo1MwIDAw0vLy+jZs2axltvvWWkpaUZhmEYsbGxxjPPPGPUrFnT8PHxMQICAozmzZsbc+fONeNli4iIiDiVLl26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5syZvPzyy5nPN2vWLN59990cZRMRkcJFhS8REZECICAgAHd3d7y9vSlVqhQAe/fuBWDMmDF06NAhc9ugoCDCwsIy/z127FgWLFjAwoULs4zauFzfvn3p1asXAG+//TaffPIJ4eHh3HXXXTnKOn78eNq1a8fw4cMBqF69Ort37+a9996jb9++REdH4+PjQ+fOnfHz86NixYo0bNgQcBS+MjIy6N69OxUrVgSgXr16Odq/3Ji0tDQ2b97M0KFDM9dZrVbat2/P+vXrs31Mamoqnp6eWdZ5eXnx559/XnU/qamppKamZv47Pj7+JpM7H2c+Xt3c3Bg9enTmvytVqsT69euZO3duZuHrzTff5MUXX+S5557L3K5p06YALF++nPDwcPbs2UP16tUBqFy58n9/Uy7j4+PD119/jbu7e+a6/v37Zy5XrlyZTz75hKZNm5KQkICvry8TJ04kICCA7777Djc3N4DMDACPP/44U6dOzSx8/fzzz6SkpGS+LhERKZpU+BIRkSLPy82F3WM6mrLf3NCkSZMs/05ISGDUqFEsWrQos5CUnJxMdHT0NZ+nfv36mcs+Pj74+/tfdYrbtezZs4f77rsvy7pbbrmFjz76CJvNRocOHahYsSKVK1fmrrvu4q677sqcshUWFka7du2oV68eHTt25M477+SBBx6gWLFiOc4hORMbG4vNZiMkJCTL+pCQkMyizeU6duzI+PHjadOmDVWqVGHFihXMnz8fm8121f2MGzcuS+ElJ8w6Vv/ed25whuN14sSJTJkyhejoaJKTk0lLS8ucnnj69GlOnDhBu3btsn1sREQE5cqVy1JwuhH16tXLUvQCx2jRUaNGsW3bNs6fP4/dbgcgOjqa2rVrExERQevWrTOLXpfr27cvw4YN46+//qJFixZMmzaNHj166MIAIiJFnHp8iYhIkWexWPB2d833m8ViyZX8l3+oe+mll1iwYAFvv/02a9asISIignr16v1nA+nLP0xaLJbMD565yc/Pjy1btvDtt99SunRpRowYQVhYGBcuXMDFxYVly5axePFiateuzYQJE6hRowZRUVG5nkNu3scff0y1atWoWbMm7u7uDB48mH79+mG1Xv0Uc+jQocTFxWXejh49et37M+tYLUzH63fffcdLL73E448/ztKlS4mIiKBfv36Z+/Py8rrm4//rfqvVesXU5PT0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",
      "text/plain": [
       "<Figure size 1500x700 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Get the plot_loss_curves() function from helper_functions.py, download the file if we don't have it\n",
    "try:\n",
    "    from helper_functions import plot_loss_curves\n",
    "except:\n",
    "    print(\"[INFO] Couldn't find helper_functions.py, downloading...\")\n",
    "    with open(\"helper_functions.py\", \"wb\") as f:\n",
    "        import requests\n",
    "        request = requests.get(\"https://raw.githubusercontent.com/mrdbourke/pytorch-deep-learning/main/helper_functions.py\")\n",
    "        f.write(request.content)\n",
    "    from helper_functions import plot_loss_curves\n",
    "\n",
    "# Plot the loss curves of our model\n",
    "plot_loss_curves(model_result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5058acff",
   "metadata": {
    "papermill": {
     "duration": 0.030456,
     "end_time": "2024-08-25T16:06:18.183164",
     "exception": false,
     "start_time": "2024-08-25T16:06:18.152708",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": []
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
   "duration": 162.676029,
   "end_time": "2024-08-25T16:06:20.989148",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2024-08-25T16:03:38.313119",
   "version": "2.6.0"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {
     "1b13e27b87cf42f58e6ba9116647b0f8": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "_model_module": "@jupyter-widgets/controls",
       "_model_module_version": "1.5.0",
       "_model_name": "DescriptionStyleModel",
       "_view_count": null,
       "_view_module": "@jupyter-widgets/base",
       "_view_module_version": "1.2.0",
       "_view_name": "StyleView",
       "description_width": ""
      }
     },
     "1b178ceb386a462a8600acc2423258a3": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "FloatProgressModel",
      "state": {
       "_dom_classes": [],
       "_model_module": "@jupyter-widgets/controls",
       "_model_module_version": "1.5.0",
       "_model_name": "FloatProgressModel",
       "_view_count": null,
       "_view_module": "@jupyter-widgets/controls",
       "_view_module_version": "1.5.0",
       "_view_name": "ProgressView",
       "bar_style": "success",
       "description": "",
       "description_tooltip": null,
       "layout": "IPY_MODEL_3b55639b8f994a879a85bdee51e96d46",
       "max": 5.0,
       "min": 0.0,
       "orientation": "horizontal",
       "style": "IPY_MODEL_2d3d824e694e4587a01273f81795388f",
       "value": 5.0
      }
     },
     "1e016fea4eca415f97dd709d5c8ed97f": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "1.2.0",
      "model_name": "LayoutModel",
      "state": {
       "_model_module": "@jupyter-widgets/base",
       "_model_module_version": "1.2.0",
       "_model_name": "LayoutModel",
       "_view_count": null,
       "_view_module": "@jupyter-widgets/base",
       "_view_module_version": "1.2.0",
       "_view_name": "LayoutView",
       "align_content": null,
       "align_items": null,
       "align_self": null,
       "border": null,
       "bottom": null,
       "display": null,
       "flex": null,
       "flex_flow": null,
       "grid_area": null,
       "grid_auto_columns": null,
       "grid_auto_flow": null,
       "grid_auto_rows": null,
       "grid_column": null,
       "grid_gap": null,
       "grid_row": null,
       "grid_template_areas": null,
       "grid_template_columns": null,
       "grid_template_rows": null,
       "height": null,
       "justify_content": null,
       "justify_items": null,
       "left": null,
       "margin": null,
       "max_height": null,
       "max_width": null,
       "min_height": null,
       "min_width": null,
       "object_fit": null,
       "object_position": null,
       "order": null,
       "overflow": null,
       "overflow_x": null,
       "overflow_y": null,
       "padding": null,
       "right": null,
       "top": null,
       "visibility": null,
       "width": null
      }
     },
     "2d3d824e694e4587a01273f81795388f": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "ProgressStyleModel",
      "state": {
       "_model_module": "@jupyter-widgets/controls",
       "_model_module_version": "1.5.0",
       "_model_name": "ProgressStyleModel",
       "_view_count": null,
       "_view_module": "@jupyter-widgets/base",
       "_view_module_version": "1.2.0",
       "_view_name": "StyleView",
       "bar_color": null,
       "description_width": ""
      }
     },
     "3b55639b8f994a879a85bdee51e96d46": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "1.2.0",
      "model_name": "LayoutModel",
      "state": {
       "_model_module": "@jupyter-widgets/base",
       "_model_module_version": "1.2.0",
       "_model_name": "LayoutModel",
       "_view_count": null,
       "_view_module": "@jupyter-widgets/base",
       "_view_module_version": "1.2.0",
       "_view_name": "LayoutView",
       "align_content": null,
       "align_items": null,
       "align_self": null,
       "border": null,
       "bottom": null,
       "display": null,
       "flex": null,
       "flex_flow": null,
       "grid_area": null,
       "grid_auto_columns": null,
       "grid_auto_flow": null,
       "grid_auto_rows": null,
       "grid_column": null,
       "grid_gap": null,
       "grid_row": null,
       "grid_template_areas": null,
       "grid_template_columns": null,
       "grid_template_rows": null,
       "height": null,
       "justify_content": null,
       "justify_items": null,
       "left": null,
       "margin": null,
       "max_height": null,
       "max_width": null,
       "min_height": null,
       "min_width": null,
       "object_fit": null,
       "object_position": null,
       "order": null,
       "overflow": null,
       "overflow_x": null,
       "overflow_y": null,
       "padding": null,
       "right": null,
       "top": null,
       "visibility": null,
       "width": null
      }
     },
     "3c0d3e1bddc646dba64575f46026657a": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "1.2.0",
      "model_name": "LayoutModel",
      "state": {
       "_model_module": "@jupyter-widgets/base",
       "_model_module_version": "1.2.0",
       "_model_name": "LayoutModel",
       "_view_count": null,
       "_view_module": "@jupyter-widgets/base",
       "_view_module_version": "1.2.0",
       "_view_name": "LayoutView",
       "align_content": null,
       "align_items": null,
       "align_self": null,
       "border": null,
       "bottom": null,
       "display": null,
       "flex": null,
       "flex_flow": null,
       "grid_area": null,
       "grid_auto_columns": null,
       "grid_auto_flow": null,
       "grid_auto_rows": null,
       "grid_column": null,
       "grid_gap": null,
       "grid_row": null,
       "grid_template_areas": null,
       "grid_template_columns": null,
       "grid_template_rows": null,
       "height": null,
       "justify_content": null,
       "justify_items": null,
       "left": null,
       "margin": null,
       "max_height": null,
       "max_width": null,
       "min_height": null,
       "min_width": null,
       "object_fit": null,
       "object_position": null,
       "order": null,
       "overflow": null,
       "overflow_x": null,
       "overflow_y": null,
       "padding": null,
       "right": null,
       "top": null,
       "visibility": null,
       "width": null
      }
     },
     "41eae9ce068b416e9f89778967806508": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "HTMLModel",
      "state": {
       "_dom_classes": [],
       "_model_module": "@jupyter-widgets/controls",
       "_model_module_version": "1.5.0",
       "_model_name": "HTMLModel",
       "_view_count": null,
       "_view_module": "@jupyter-widgets/controls",
       "_view_module_version": "1.5.0",
       "_view_name": "HTMLView",
       "description": "",
       "description_tooltip": null,
       "layout": "IPY_MODEL_3c0d3e1bddc646dba64575f46026657a",
       "placeholder": "​",
       "style": "IPY_MODEL_1b13e27b87cf42f58e6ba9116647b0f8",
       "value": "100%"
      }
     },
     "86fb4e480b114f8a8bfd05b4e263d2e1": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "HTMLModel",
      "state": {
       "_dom_classes": [],
       "_model_module": "@jupyter-widgets/controls",
       "_model_module_version": "1.5.0",
       "_model_name": "HTMLModel",
       "_view_count": null,
       "_view_module": "@jupyter-widgets/controls",
       "_view_module_version": "1.5.0",
       "_view_name": "HTMLView",
       "description": "",
       "description_tooltip": null,
       "layout": "IPY_MODEL_dc7975b05617442c804a8410263d3a7b",
       "placeholder": "​",
       "style": "IPY_MODEL_e1c2affa8f9b46ef828fe2f0e6d3ca7a",
       "value": " 5/5 [01:35&lt;00:00, 19.28s/it]"
      }
     },
     "906e09f0a4e04938a00ba725d25db39d": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "HBoxModel",
      "state": {
       "_dom_classes": [],
       "_model_module": "@jupyter-widgets/controls",
       "_model_module_version": "1.5.0",
       "_model_name": "HBoxModel",
       "_view_count": null,
       "_view_module": "@jupyter-widgets/controls",
       "_view_module_version": "1.5.0",
       "_view_name": "HBoxView",
       "box_style": "",
       "children": [
        "IPY_MODEL_41eae9ce068b416e9f89778967806508",
        "IPY_MODEL_1b178ceb386a462a8600acc2423258a3",
        "IPY_MODEL_86fb4e480b114f8a8bfd05b4e263d2e1"
       ],
       "layout": "IPY_MODEL_1e016fea4eca415f97dd709d5c8ed97f"
      }
     },
     "dc7975b05617442c804a8410263d3a7b": {
      "model_module": "@jupyter-widgets/base",
      "model_module_version": "1.2.0",
      "model_name": "LayoutModel",
      "state": {
       "_model_module": "@jupyter-widgets/base",
       "_model_module_version": "1.2.0",
       "_model_name": "LayoutModel",
       "_view_count": null,
       "_view_module": "@jupyter-widgets/base",
       "_view_module_version": "1.2.0",
       "_view_name": "LayoutView",
       "align_content": null,
       "align_items": null,
       "align_self": null,
       "border": null,
       "bottom": null,
       "display": null,
       "flex": null,
       "flex_flow": null,
       "grid_area": null,
       "grid_auto_columns": null,
       "grid_auto_flow": null,
       "grid_auto_rows": null,
       "grid_column": null,
       "grid_gap": null,
       "grid_row": null,
       "grid_template_areas": null,
       "grid_template_columns": null,
       "grid_template_rows": null,
       "height": null,
       "justify_content": null,
       "justify_items": null,
       "left": null,
       "margin": null,
       "max_height": null,
       "max_width": null,
       "min_height": null,
       "min_width": null,
       "object_fit": null,
       "object_position": null,
       "order": null,
       "overflow": null,
       "overflow_x": null,
       "overflow_y": null,
       "padding": null,
       "right": null,
       "top": null,
       "visibility": null,
       "width": null
      }
     },
     "e1c2affa8f9b46ef828fe2f0e6d3ca7a": {
      "model_module": "@jupyter-widgets/controls",
      "model_module_version": "1.5.0",
      "model_name": "DescriptionStyleModel",
      "state": {
       "_model_module": "@jupyter-widgets/controls",
       "_model_module_version": "1.5.0",
       "_model_name": "DescriptionStyleModel",
       "_view_count": null,
       "_view_module": "@jupyter-widgets/base",
       "_view_module_version": "1.2.0",
       "_view_name": "StyleView",
       "description_width": ""
      }
     }
    },
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
