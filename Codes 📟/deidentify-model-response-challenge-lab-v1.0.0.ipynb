{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c786c559-55b7-4378-a109-f9895cffd086",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Copyright 2023 Google LLC\n",
    "#\n",
    "# Licensed under the Apache License, Version 2.0 (the \"License\");\n",
    "# you may not use this file except in compliance with the License.\n",
    "# You may obtain a copy of the License at\n",
    "#\n",
    "#     https://www.apache.org/licenses/LICENSE-2.0\n",
    "#\n",
    "# Unless required by applicable law or agreed to in writing, software\n",
    "# distributed under the License is distributed on an \"AS IS\" BASIS,\n",
    "# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
    "# See the License for the specific language governing permissions and\n",
    "# limitations under the License."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "79cf3796-4504-44e2-893b-457d4f6028ee",
   "metadata": {},
   "source": [
    "# Protecting Sensitive Data in Gen AI model responses"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dffe023b-380e-4b0d-8a24-bdf6fce600c0",
   "metadata": {},
   "source": [
    "## Overview\n",
    "\n",
    "Your team already has a Python function that identifies and redacts or blocks sensitive data types in Gen AI model responses. You have been asked to expand the function to block Gen AI model responses that contain [US Vehicle Identification Numbers](https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference#united_states), which are sensitive data consisting of a unique 17-digit code assigned to every on-road motor vehicle in North America. \n",
    "\n",
    "To help you achieve this goal, complete the following subtasks by following the instructions in the cells below:\n",
    "\n",
    "1. Run all cells in the section titled Getting started with this notebook. \n",
    "\n",
    "2. Expand an existing Python function in the section titled Update an existing Python function to block Gemini 2.0 Flash model responses when a US VIN has been included.\n",
    "\n",
    "3. Generate an example text response with the following prompt to test your updated function: `Is 4Y1SL65848Z411439 an example of a US Vehicle Identification Number (VIN)?`"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "14eac4fa-8017-4f16-8a2b-2cd0a5d8f1ad",
   "metadata": {
    "tags": []
   },
   "source": [
    "## Getting started with this notebook\n",
    "\n",
    "Below are few steps to get your environment ready, including installing key Python packages and setting your environmental variables (project ID and region). \n",
    "\n",
    "Be sure to run each cell in consecutive order using the `Run` button (play arrow) at the top of this notebook. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "09dbab5b-e2f1-40de-a13a-8a6dec8713a7",
   "metadata": {},
   "source": [
    "### Install necessary packages "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cf41e1a4-6eae-44dd-b4de-d628cade341e",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: google-cloud-aiplatform in /opt/conda/lib/python3.10/site-packages (1.130.0)\n",
      "Collecting google-cloud-aiplatform\n",
      "  Downloading google_cloud_aiplatform-1.132.0-py2.py3-none-any.whl.metadata (46 kB)\n",
      "Requirement already satisfied: google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0,>=1.34.1 in /opt/conda/lib/python3.10/site-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0,>=1.34.1->google-cloud-aiplatform) (2.28.1)\n",
      "Collecting google-auth<3.0.0,>=2.45.0 (from google-cloud-aiplatform)\n",
      "  Downloading google_auth-2.45.0-py2.py3-none-any.whl.metadata (6.8 kB)\n",
      "Requirement already satisfied: proto-plus<2.0.0,>=1.22.3 in /opt/conda/lib/python3.10/site-packages (from google-cloud-aiplatform) (1.26.1)\n",
      "Requirement already satisfied: protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<7.0.0,>=3.20.2 in /opt/conda/lib/python3.10/site-packages (from google-cloud-aiplatform) (6.33.2)\n",
      "Requirement already satisfied: packaging>=14.3 in /opt/conda/lib/python3.10/site-packages (from google-cloud-aiplatform) (25.0)\n",
      "Requirement already satisfied: google-cloud-storage<4.0.0,>=1.32.0 in /opt/conda/lib/python3.10/site-packages (from google-cloud-aiplatform) (3.7.0)\n",
      "Requirement already satisfied: google-cloud-bigquery!=3.20.0,<4.0.0,>=1.15.0 in /opt/conda/lib/python3.10/site-packages (from google-cloud-aiplatform) (3.38.0)\n",
      "Requirement already satisfied: google-cloud-resource-manager<3.0.0,>=1.3.3 in /opt/conda/lib/python3.10/site-packages (from google-cloud-aiplatform) (1.15.0)\n",
      "Requirement already satisfied: shapely<3.0.0 in /opt/conda/lib/python3.10/site-packages (from google-cloud-aiplatform) (2.1.2)\n",
      "Requirement already satisfied: google-genai<2.0.0,>=1.37.0 in /opt/conda/lib/python3.10/site-packages (from google-cloud-aiplatform) (1.55.0)\n",
      "Requirement already satisfied: pydantic<3 in /opt/conda/lib/python3.10/site-packages (from google-cloud-aiplatform) (2.12.5)\n",
      "Requirement already satisfied: typing_extensions in /opt/conda/lib/python3.10/site-packages (from google-cloud-aiplatform) (4.15.0)\n",
      "Requirement already satisfied: docstring_parser<1 in /opt/conda/lib/python3.10/site-packages (from google-cloud-aiplatform) (0.17.0)\n",
      "Requirement already satisfied: googleapis-common-protos<2.0.0,>=1.56.2 in /opt/conda/lib/python3.10/site-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0,>=1.34.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0,>=1.34.1->google-cloud-aiplatform) (1.72.0)\n",
      "Requirement already satisfied: requests<3.0.0,>=2.18.0 in /opt/conda/lib/python3.10/site-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0,>=1.34.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0,>=1.34.1->google-cloud-aiplatform) (2.32.5)\n",
      "Requirement already satisfied: grpcio<2.0.0,>=1.33.2 in /opt/conda/lib/python3.10/site-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0,>=1.34.1->google-cloud-aiplatform) (1.76.0)\n",
      "Requirement already satisfied: grpcio-status<2.0.0,>=1.33.2 in /opt/conda/lib/python3.10/site-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0,>=1.34.1->google-cloud-aiplatform) (1.76.0)\n",
      "Requirement already satisfied: cachetools<7.0,>=2.0.0 in /opt/conda/lib/python3.10/site-packages (from google-auth<3.0.0,>=2.45.0->google-cloud-aiplatform) (6.2.2)\n",
      "Requirement already satisfied: pyasn1-modules>=0.2.1 in /opt/conda/lib/python3.10/site-packages (from google-auth<3.0.0,>=2.45.0->google-cloud-aiplatform) (0.4.2)\n",
      "Requirement already satisfied: rsa<5,>=3.1.4 in /opt/conda/lib/python3.10/site-packages (from google-auth<3.0.0,>=2.45.0->google-cloud-aiplatform) (4.9.1)\n",
      "Requirement already satisfied: google-cloud-core<3.0.0,>=2.4.1 in /opt/conda/lib/python3.10/site-packages (from google-cloud-bigquery!=3.20.0,<4.0.0,>=1.15.0->google-cloud-aiplatform) (2.5.0)\n",
      "Requirement already satisfied: google-resumable-media<3.0.0,>=2.0.0 in /opt/conda/lib/python3.10/site-packages (from google-cloud-bigquery!=3.20.0,<4.0.0,>=1.15.0->google-cloud-aiplatform) (2.8.0)\n",
      "Requirement already satisfied: python-dateutil<3.0.0,>=2.8.2 in /opt/conda/lib/python3.10/site-packages (from google-cloud-bigquery!=3.20.0,<4.0.0,>=1.15.0->google-cloud-aiplatform) (2.9.0.post0)\n",
      "Requirement already satisfied: grpc-google-iam-v1<1.0.0,>=0.14.0 in /opt/conda/lib/python3.10/site-packages (from google-cloud-resource-manager<3.0.0,>=1.3.3->google-cloud-aiplatform) (0.14.3)\n",
      "Requirement already satisfied: google-crc32c<2.0.0,>=1.1.3 in /opt/conda/lib/python3.10/site-packages (from google-cloud-storage<4.0.0,>=1.32.0->google-cloud-aiplatform) (1.7.1)\n",
      "Requirement already satisfied: anyio<5.0.0,>=4.8.0 in /opt/conda/lib/python3.10/site-packages (from google-genai<2.0.0,>=1.37.0->google-cloud-aiplatform) (4.12.0)\n",
      "Requirement already satisfied: httpx<1.0.0,>=0.28.1 in /opt/conda/lib/python3.10/site-packages (from google-genai<2.0.0,>=1.37.0->google-cloud-aiplatform) (0.28.1)\n",
      "Requirement already satisfied: tenacity<9.2.0,>=8.2.3 in /opt/conda/lib/python3.10/site-packages (from google-genai<2.0.0,>=1.37.0->google-cloud-aiplatform) (9.1.2)\n",
      "Requirement already satisfied: websockets<15.1.0,>=13.0.0 in /opt/conda/lib/python3.10/site-packages (from google-genai<2.0.0,>=1.37.0->google-cloud-aiplatform) (15.0.1)\n",
      "Requirement already satisfied: distro<2,>=1.7.0 in /opt/conda/lib/python3.10/site-packages (from google-genai<2.0.0,>=1.37.0->google-cloud-aiplatform) (1.9.0)\n",
      "Requirement already satisfied: sniffio in /opt/conda/lib/python3.10/site-packages (from google-genai<2.0.0,>=1.37.0->google-cloud-aiplatform) (1.3.1)\n",
      "Requirement already satisfied: exceptiongroup>=1.0.2 in /opt/conda/lib/python3.10/site-packages (from anyio<5.0.0,>=4.8.0->google-genai<2.0.0,>=1.37.0->google-cloud-aiplatform) (1.3.1)\n",
      "Requirement already satisfied: idna>=2.8 in /opt/conda/lib/python3.10/site-packages (from anyio<5.0.0,>=4.8.0->google-genai<2.0.0,>=1.37.0->google-cloud-aiplatform) (3.11)\n",
      "Requirement already satisfied: certifi in /opt/conda/lib/python3.10/site-packages (from httpx<1.0.0,>=0.28.1->google-genai<2.0.0,>=1.37.0->google-cloud-aiplatform) (2025.11.12)\n",
      "Requirement already satisfied: httpcore==1.* in /opt/conda/lib/python3.10/site-packages (from httpx<1.0.0,>=0.28.1->google-genai<2.0.0,>=1.37.0->google-cloud-aiplatform) (1.0.9)\n",
      "Requirement already satisfied: h11>=0.16 in /opt/conda/lib/python3.10/site-packages (from httpcore==1.*->httpx<1.0.0,>=0.28.1->google-genai<2.0.0,>=1.37.0->google-cloud-aiplatform) (0.16.0)\n",
      "Requirement already satisfied: annotated-types>=0.6.0 in /opt/conda/lib/python3.10/site-packages (from pydantic<3->google-cloud-aiplatform) (0.7.0)\n",
      "Requirement already satisfied: pydantic-core==2.41.5 in /opt/conda/lib/python3.10/site-packages (from pydantic<3->google-cloud-aiplatform) (2.41.5)\n",
      "Requirement already satisfied: typing-inspection>=0.4.2 in /opt/conda/lib/python3.10/site-packages (from pydantic<3->google-cloud-aiplatform) (0.4.2)\n",
      "Requirement already satisfied: six>=1.5 in /opt/conda/lib/python3.10/site-packages (from python-dateutil<3.0.0,>=2.8.2->google-cloud-bigquery!=3.20.0,<4.0.0,>=1.15.0->google-cloud-aiplatform) (1.17.0)\n",
      "Requirement already satisfied: charset_normalizer<4,>=2 in /opt/conda/lib/python3.10/site-packages (from requests<3.0.0,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0,>=1.34.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0,>=1.34.1->google-cloud-aiplatform) (3.4.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in /opt/conda/lib/python3.10/site-packages (from requests<3.0.0,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0,>=1.34.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,<3.0.0,>=1.34.1->google-cloud-aiplatform) (2.6.1)\n",
      "Requirement already satisfied: pyasn1>=0.1.3 in /opt/conda/lib/python3.10/site-packages (from rsa<5,>=3.1.4->google-auth<3.0.0,>=2.45.0->google-cloud-aiplatform) (0.6.1)\n",
      "Requirement already satisfied: numpy>=1.21 in /opt/conda/lib/python3.10/site-packages (from shapely<3.0.0->google-cloud-aiplatform) (1.26.4)\n",
      "Downloading google_cloud_aiplatform-1.132.0-py2.py3-none-any.whl (8.2 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.2/8.2 MB\u001b[0m \u001b[31m19.8 MB/s\u001b[0m  \u001b[33m0:00:00\u001b[0mm0:00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hDownloading google_auth-2.45.0-py2.py3-none-any.whl (233 kB)\n",
      "Installing collected packages: google-auth, google-cloud-aiplatform\n",
      "\u001b[2K   \u001b[91m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[90m╺\u001b[0m\u001b[90m━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1/2\u001b[0m [google-cloud-aiplatform]\u001b[33m  WARNING: The script tb-gcp-uploader is installed in '/home/jupyter/.local/bin' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\u001b[0m\u001b[33m\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2/2\u001b[0m [google-cloud-aiplatform]\n",
      "\u001b[1A\u001b[2KSuccessfully installed google-auth-2.45.0 google-cloud-aiplatform-1.132.0\n",
      "Collecting google-cloud-dlp\n",
      "  Downloading google_cloud_dlp-3.33.0-py3-none-any.whl.metadata (9.9 kB)\n",
      "Requirement already satisfied: google-api-core!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0,>=1.34.1 in /opt/conda/lib/python3.10/site-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0,>=1.34.1->google-cloud-dlp) (2.28.1)\n",
      "Requirement already satisfied: google-auth!=2.24.0,!=2.25.0,<3.0.0,>=2.14.1 in ./.local/lib/python3.10/site-packages (from google-cloud-dlp) (2.45.0)\n",
      "Requirement already satisfied: grpcio<2.0.0,>=1.33.2 in /opt/conda/lib/python3.10/site-packages (from google-cloud-dlp) (1.76.0)\n",
      "Requirement already satisfied: proto-plus<2.0.0,>=1.22.3 in /opt/conda/lib/python3.10/site-packages (from google-cloud-dlp) (1.26.1)\n",
      "Requirement already satisfied: protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<7.0.0,>=3.20.2 in /opt/conda/lib/python3.10/site-packages (from google-cloud-dlp) (6.33.2)\n",
      "Requirement already satisfied: googleapis-common-protos<2.0.0,>=1.56.2 in /opt/conda/lib/python3.10/site-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0,>=1.34.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0,>=1.34.1->google-cloud-dlp) (1.72.0)\n",
      "Requirement already satisfied: requests<3.0.0,>=2.18.0 in /opt/conda/lib/python3.10/site-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0,>=1.34.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0,>=1.34.1->google-cloud-dlp) (2.32.5)\n",
      "Requirement already satisfied: grpcio-status<2.0.0,>=1.33.2 in /opt/conda/lib/python3.10/site-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0,>=1.34.1->google-cloud-dlp) (1.76.0)\n",
      "Requirement already satisfied: cachetools<7.0,>=2.0.0 in /opt/conda/lib/python3.10/site-packages (from google-auth!=2.24.0,!=2.25.0,<3.0.0,>=2.14.1->google-cloud-dlp) (6.2.2)\n",
      "Requirement already satisfied: pyasn1-modules>=0.2.1 in /opt/conda/lib/python3.10/site-packages (from google-auth!=2.24.0,!=2.25.0,<3.0.0,>=2.14.1->google-cloud-dlp) (0.4.2)\n",
      "Requirement already satisfied: rsa<5,>=3.1.4 in /opt/conda/lib/python3.10/site-packages (from google-auth!=2.24.0,!=2.25.0,<3.0.0,>=2.14.1->google-cloud-dlp) (4.9.1)\n",
      "Requirement already satisfied: typing-extensions~=4.12 in /opt/conda/lib/python3.10/site-packages (from grpcio<2.0.0,>=1.33.2->google-cloud-dlp) (4.15.0)\n",
      "Requirement already satisfied: charset_normalizer<4,>=2 in /opt/conda/lib/python3.10/site-packages (from requests<3.0.0,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0,>=1.34.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0,>=1.34.1->google-cloud-dlp) (3.4.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /opt/conda/lib/python3.10/site-packages (from requests<3.0.0,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0,>=1.34.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0,>=1.34.1->google-cloud-dlp) (3.11)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in /opt/conda/lib/python3.10/site-packages (from requests<3.0.0,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0,>=1.34.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0,>=1.34.1->google-cloud-dlp) (2.6.1)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /opt/conda/lib/python3.10/site-packages (from requests<3.0.0,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0,>=1.34.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0,>=1.34.1->google-cloud-dlp) (2025.11.12)\n",
      "Requirement already satisfied: pyasn1>=0.1.3 in /opt/conda/lib/python3.10/site-packages (from rsa<5,>=3.1.4->google-auth!=2.24.0,!=2.25.0,<3.0.0,>=2.14.1->google-cloud-dlp) (0.6.1)\n",
      "Downloading google_cloud_dlp-3.33.0-py3-none-any.whl (218 kB)\n",
      "Installing collected packages: google-cloud-dlp\n",
      "Successfully installed google-cloud-dlp-3.33.0\n"
     ]
    }
   ],
   "source": [
    "# Install Vertex AI\n",
    "!pip install google-cloud-aiplatform --upgrade --user\n",
    "\n",
    "# Install Cloud Data Loss Prevention\n",
    "! pip install google-cloud-dlp --upgrade --user"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "74674658-3cf1-4cda-9048-d52a4a8dc171",
   "metadata": {},
   "source": [
    "### Restart current runtime\n",
    "\n",
    "To use the newly installed packages in this Jupyter runtime, you must restart the runtime. You can do this by running the cell below, which will restart the current kernel."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f48dd97c-5ead-41e5-a006-0f8102171f03",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'status': 'ok', 'restart': True}"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Restart kernel after installs so that your environment can access the new packages\n",
    "import IPython\n",
    "\n",
    "app = IPython.Application.instance()\n",
    "app.kernel.do_shutdown(True)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "57fd18cb-dd00-487a-a908-dc5327c7ada5",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-warning\">\n",
    "<b><p>⚠️ The kernel is going to restart. Please wait until it is finished before continuing to the next step. ⚠️</p> When prompted, click OK to continue. </b>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "64e74c8c-8267-43f8-bdc1-e94b32ef81cd",
   "metadata": {},
   "source": [
    "### Set your project ID and region"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6cc70244-486b-4104-b9ca-74965fbcfff0",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "qwiklabs-gcp-03-e318e47ac120\n",
      "us-west1\n"
     ]
    }
   ],
   "source": [
    "# Get the Project ID\n",
    "PROJECT_ID = !gcloud config get project  # Example: qwiklabs-gcp-04-b75c09c1eb74\n",
    "PROJECT_ID = PROJECT_ID[0]\n",
    "print(PROJECT_ID)  # Print the Project ID\n",
    "\n",
    "# Get the default region\n",
    "LOCATION = !gcloud compute project-info describe --format=\"value(commonInstanceMetadata.items[google-compute-default-region])\"\n",
    "print(LOCATION[0])  # Print the region (e.g., us-central1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5063620e-85b3-4775-b8c0-cec8edaf2ae9",
   "metadata": {
    "tags": []
   },
   "source": [
    "### Import Gemini 2.0 Flash model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "771ffbb4-a600-468b-a143-59a7d88e5db3",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/conda/lib/python3.10/site-packages/google/api_core/_python_version_support.py:266: FutureWarning: You are using a Python version (3.10.19) which Google will stop supporting in new releases of google.cloud.aiplatform_v1beta1 once it reaches its end of life (2026-10-04). Please upgrade to the latest Python version, or at least Python 3.11, to continue receiving updates for google.cloud.aiplatform_v1beta1 past that date.\n",
      "  warnings.warn(message, FutureWarning)\n",
      "/opt/conda/lib/python3.10/site-packages/google/api_core/_python_version_support.py:266: FutureWarning: You are using a Python version (3.10.19) which Google will stop supporting in new releases of google.cloud.aiplatform_v1 once it reaches its end of life (2026-10-04). Please upgrade to the latest Python version, or at least Python 3.11, to continue receiving updates for google.cloud.aiplatform_v1 past that date.\n",
      "  warnings.warn(message, FutureWarning)\n",
      "/opt/conda/lib/python3.10/site-packages/google/api_core/_python_version_support.py:266: FutureWarning: You are using a Python version (3.10.19) which Google will stop supporting in new releases of google.cloud.aiplatform.v1.schema.predict.instance_v1 once it reaches its end of life (2026-10-04). Please upgrade to the latest Python version, or at least Python 3.11, to continue receiving updates for google.cloud.aiplatform.v1.schema.predict.instance_v1 past that date.\n",
      "  warnings.warn(message, FutureWarning)\n",
      "/opt/conda/lib/python3.10/site-packages/google/api_core/_python_version_support.py:266: FutureWarning: You are using a Python version (3.10.19) which Google will stop supporting in new releases of google.cloud.aiplatform.v1.schema.predict.params_v1 once it reaches its end of life (2026-10-04). Please upgrade to the latest Python version, or at least Python 3.11, to continue receiving updates for google.cloud.aiplatform.v1.schema.predict.params_v1 past that date.\n",
      "  warnings.warn(message, FutureWarning)\n",
      "/opt/conda/lib/python3.10/site-packages/google/api_core/_python_version_support.py:266: FutureWarning: You are using a Python version (3.10.19) which Google will stop supporting in new releases of google.cloud.aiplatform.v1.schema.predict.prediction_v1 once it reaches its end of life (2026-10-04). Please upgrade to the latest Python version, or at least Python 3.11, to continue receiving updates for google.cloud.aiplatform.v1.schema.predict.prediction_v1 past that date.\n",
      "  warnings.warn(message, FutureWarning)\n",
      "/opt/conda/lib/python3.10/site-packages/google/api_core/_python_version_support.py:266: FutureWarning: You are using a Python version (3.10.19) which Google will stop supporting in new releases of google.cloud.aiplatform.v1.schema.trainingjob.definition_v1 once it reaches its end of life (2026-10-04). Please upgrade to the latest Python version, or at least Python 3.11, to continue receiving updates for google.cloud.aiplatform.v1.schema.trainingjob.definition_v1 past that date.\n",
      "  warnings.warn(message, FutureWarning)\n",
      "/opt/conda/lib/python3.10/site-packages/google/api_core/_python_version_support.py:266: FutureWarning: You are using a Python version (3.10.19) which Google will stop supporting in new releases of google.cloud.aiplatform.v1beta1.schema.predict.instance_v1beta1 once it reaches its end of life (2026-10-04). Please upgrade to the latest Python version, or at least Python 3.11, to continue receiving updates for google.cloud.aiplatform.v1beta1.schema.predict.instance_v1beta1 past that date.\n",
      "  warnings.warn(message, FutureWarning)\n",
      "/opt/conda/lib/python3.10/site-packages/google/api_core/_python_version_support.py:266: FutureWarning: You are using a Python version (3.10.19) which Google will stop supporting in new releases of google.cloud.aiplatform.v1beta1.schema.predict.params_v1beta1 once it reaches its end of life (2026-10-04). Please upgrade to the latest Python version, or at least Python 3.11, to continue receiving updates for google.cloud.aiplatform.v1beta1.schema.predict.params_v1beta1 past that date.\n",
      "  warnings.warn(message, FutureWarning)\n",
      "/opt/conda/lib/python3.10/site-packages/google/api_core/_python_version_support.py:266: FutureWarning: You are using a Python version (3.10.19) which Google will stop supporting in new releases of google.cloud.aiplatform.v1beta1.schema.predict.prediction_v1beta1 once it reaches its end of life (2026-10-04). Please upgrade to the latest Python version, or at least Python 3.11, to continue receiving updates for google.cloud.aiplatform.v1beta1.schema.predict.prediction_v1beta1 past that date.\n",
      "  warnings.warn(message, FutureWarning)\n",
      "/opt/conda/lib/python3.10/site-packages/google/api_core/_python_version_support.py:266: FutureWarning: You are using a Python version (3.10.19) which Google will stop supporting in new releases of google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1 once it reaches its end of life (2026-10-04). Please upgrade to the latest Python version, or at least Python 3.11, to continue receiving updates for google.cloud.aiplatform.v1beta1.schema.trainingjob.definition_v1beta1 past that date.\n",
      "  warnings.warn(message, FutureWarning)\n",
      "/home/jupyter/.local/lib/python3.10/site-packages/vertexai/generative_models/_generative_models.py:433: UserWarning: This feature is deprecated as of June 24, 2025 and will be removed on June 24, 2026. For details, see https://cloud.google.com/vertex-ai/generative-ai/docs/deprecations/genai-vertexai-sdk.\n",
      "  warning_logs.show_deprecation_warning()\n"
     ]
    }
   ],
   "source": [
    "# Import model for text generation\n",
    "from vertexai.generative_models import GenerativeModel\n",
    "model = GenerativeModel(\"gemini-2.0-flash-001\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2e5239cb-d8e1-4c2f-852c-a0ce3556c2ec",
   "metadata": {
    "tags": []
   },
   "source": [
    "## Update an existing Python function to block Gemini 2.0 Flash model responses when a US VIN has been included\n",
    "\n",
    "In this section, you revise an existing Python function to block output for [US Vehicle Identification Numbers (last entry for United States infoTypes)](https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference#united_states).\n",
    "\n",
    "In the code block below for the function, __modify the code lines after `# Add conditional return to block responses containing US Vehicle Identification Numbers (VIN)`__ to block model responses containing this infoType.\n",
    "\n",
    "Be sure to run the cell with your final Python function code before you move onto the next cells to test the updated function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "da6b40ac-c8e8-4dbf-8dac-3ecfacaedb91",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Redefine original function to inspect and deidentify output with Sensitive Data Protection\n",
    "import google.cloud.dlp  \n",
    "from typing import List \n",
    "\n",
    "def deidentify_with_replace_infotype(\n",
    "    project: str, item: str, info_types: List[str]\n",
    ") -> None:\n",
    "    \"\"\"Uses the Data Loss Prevention API to deidentify sensitive data in a\n",
    "    string by replacing it with the info type.\n",
    "    Args:\n",
    "        project: The Google Cloud project id to use as a parent resource.\n",
    "        item: The string to deidentify (will be treated as text).\n",
    "        info_types: A list of strings representing info types to look for.\n",
    "            A full list of info type categories can be fetched from the API.\n",
    "    Returns:\n",
    "        None; the response from the API is printed to the terminal.\n",
    "    \"\"\"\n",
    "\n",
    "    # Instantiate a client\n",
    "    dlp = google.cloud.dlp_v2.DlpServiceClient()\n",
    "\n",
    "    # Convert the project id into a full resource id.\n",
    "    parent = f\"projects/{PROJECT_ID}\"\n",
    "\n",
    "    # Construct inspect configuration dictionary\n",
    "    inspect_config = {\"info_types\": [{\"name\": info_type} for info_type in info_types]}\n",
    "\n",
    "    # Construct deidentify configuration dictionary\n",
    "    deidentify_config = {\n",
    "        \"info_type_transformations\": {\n",
    "            \"transformations\": [\n",
    "                {\"primitive_transformation\": {\"replace_with_info_type_config\": {}}}\n",
    "            ]\n",
    "        }\n",
    "    }\n",
    "\n",
    "    # Call the API for deidentify\n",
    "    response = dlp.deidentify_content(\n",
    "        request={\n",
    "            \"parent\": parent,\n",
    "            \"deidentify_config\": deidentify_config,\n",
    "            \"inspect_config\": inspect_config,\n",
    "            \"item\": {\"value\": item},\n",
    "        }\n",
    "    )\n",
    "\n",
    "    return_payload = response.item.value\n",
    "    \n",
    "    # Add conditional return to block responses containing US Vehicle Identification Numbers (VIN)\n",
    "    info_types = [\"DOCUMENT_TYPE/R&D/SOURCE_CODE\"]\n",
    "    inspect_config = {\"info_types\": [{\"name\": info_type} for info_type in info_types]}\n",
    "\n",
    "    response = dlp.inspect_content(\n",
    "        request={\n",
    "            \"parent\": parent,\n",
    "            \"inspect_config\": inspect_config,\n",
    "            \"item\": {\"value\": item},\n",
    "        }\n",
    "    )\n",
    "\n",
    "    if response.result.findings:\n",
    "        for finding in response.result.findings:\n",
    "            if finding.info_type.name == \"DOCUMENT_TYPE/R&D/SOURCE_CODE\":\n",
    "                return_payload = '[Blocked due to category: Source Code]'\n",
    "                \n",
    "    # Print results\n",
    "    print(return_payload)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1fcc9d0c-3fcb-48a5-9964-1947dadb10b9",
   "metadata": {},
   "source": [
    "## Generate an example with VIN using Gemini 2.0 Flash model and block results\n",
    "\n",
    "In the code blocks below, generate an example text response containing a US Vehicle Identification Number (VIN) using the following prompt:\n",
    "\n",
    "`Is 4Y1SL65848Z411439 an example of a US Vehicle Identification Number (VIN)?`\n",
    "\n",
    "Then, write and execute the appropriate code lines to block responses containing US Vehicle Identification Numbers (VIN). "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "cb204161-0c3a-417c-b5f7-86b3b3e6b677",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No, that is not a valid US VIN. Here's why:\n",
      "\n",
      "*   **Length:** A valid VIN is exactly 17 characters long. The provided string is 17 characters long, which at least passes this basic test.\n",
      "*   **Characters:** A VIN uses uppercase letters (A-Z) and digits (0-9) *excluding* the letters I, O, and Q. There are no invalid characters here.\n",
      "*   **Check Digit:** The 9th position is a check digit, calculated based on the other characters in the VIN. It's very unlikely a randomly generated string would have a valid check digit. It would have to be tested against a VIN decoder to be validated, which requires specific software or algorithms and would not be possible for me to perform in this context.\n",
      "*   **WMI Code:** The first 3 positions of a VIN represent the WMI (World Manufacturer Identifier). It should be a valid identifier in the VIN system. It is unlikely that 4Y1 would be a real WMI Code.\n",
      "\n",
      "Therefore, while the length and allowed characters seem correct, it is highly probable that the provided string is an invalid VIN due to the unlikely chance of a valid check digit and a valid WMI Code.\n",
      "[Blocked due to category: Source Code]\n"
     ]
    }
   ],
   "source": [
    "# Create prompt that generates an example response with US Vehicle Identification Number (VIN)\n",
    "prompt = \"Is 4Y1SL65848Z411439 an example of a US Vehicle Identification Number (VIN)?\"\n",
    "\n",
    "# Run model with prompt\n",
    "# Name the output as response_vin\n",
    "response_vin = model.generate_content(prompt)\n",
    "\n",
    "# Print response without blocking it (VIN provided)\n",
    "print(response_vin.text)\n",
    "\n",
    "# Block model response that includes US Vehicle Identification Number (VIN)\n",
    "deidentify_with_replace_infotype(\n",
    "    project=PROJECT_ID,\n",
    "    item=response_vin.text,\n",
    "    info_types=[\"US_VEHICLE_IDENTIFICATION_NUMBER\"]\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5dba6d7a-ad2b-495d-a05f-53ee63d07832",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def deidentify_with_replace_infotype(\n",
    "    project: str, item: str, info_types: List[str]\n",
    ") -> None:\n",
    "    \"\"\"Uses the Data Loss Prevention API to deidentify sensitive data in a\n",
    "    string by replacing it with the info type.\n",
    "    Args:\n",
    "        project: The Google Cloud project id to use as a parent resource.\n",
    "        item: The string to deidentify (will be treated as text).\n",
    "        info_types: A list of strings representing info types to look for.\n",
    "            A full list of info type categories can be fetched from the API.\n",
    "    Returns:\n",
    "        None; the response from the API is printed to the terminal.\n",
    "    \"\"\"\n",
    "\n",
    "    # Instantiate a client\n",
    "    dlp = google.cloud.dlp_v2.DlpServiceClient()\n",
    "\n",
    "    # Convert the project id into a full resource id.\n",
    "    parent = f\"projects/{PROJECT_ID}\"\n",
    "\n",
    "    # Construct inspect configuration dictionary\n",
    "    inspect_config = {\"info_types\": [{\"name\": info_type} for info_type in info_types]}\n",
    "\n",
    "    # Construct deidentify configuration dictionary\n",
    "    deidentify_config = {\n",
    "        \"info_type_transformations\": {\n",
    "            \"transformations\": [\n",
    "                {\"primitive_transformation\": {\"replace_with_info_type_config\": {}}}\n",
    "            ]\n",
    "        }\n",
    "    }\n",
    "\n",
    "    # Call the API for deidentify\n",
    "    response = dlp.deidentify_content(\n",
    "        request={\n",
    "            \"parent\": parent,\n",
    "            \"deidentify_config\": deidentify_config,\n",
    "            \"inspect_config\": inspect_config,\n",
    "            \"item\": {\"value\": item},\n",
    "        }\n",
    "    )\n",
    "\n",
    "    return_payload = response.item.value\n",
    "    \n",
    "    # Add conditional return to block responses containing US Vehicle Identification Numbers (VIN)\n",
    "    vin_info_types = [\"US_VEHICLE_IDENTIFICATION_NUMBER\"]\n",
    "    inspect_config = {\"info_types\": [{\"name\": info_type} for info_type in vin_info_types]}\n",
    "\n",
    "    response = dlp.inspect_content(\n",
    "        request={\n",
    "            \"parent\": parent,\n",
    "            \"inspect_config\": inspect_config,\n",
    "            \"item\": {\"value\": item},\n",
    "        }\n",
    "    )\n",
    "\n",
    "    if response.result.findings:\n",
    "        for finding in response.result.findings:\n",
    "            if finding.info_type.name == \"US_VEHICLE_IDENTIFICATION_NUMBER\":\n",
    "                return_payload = '[Blocked due to category: US Vehicle Identification Number (VIN)]'\n",
    "                \n",
    "    # Print results\n",
    "    print(return_payload)"
   ]
  }
 ],
 "metadata": {
  "environment": {
   "kernel": "conda-base-py",
   "name": "workbench-notebooks.m137",
   "type": "gcloud",
   "uri": "us-docker.pkg.dev/deeplearning-platform-release/gcr.io/workbench-notebooks:m137"
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel) (Local)",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.10.19"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
