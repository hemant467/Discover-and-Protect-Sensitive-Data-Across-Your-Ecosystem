{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c786c559-55b7-4378-a109-f9895cffd086",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Copyright 2025 Google LLC\n",
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
    "2. Expand an existing Python function in the section titled Update an existing Python function to block Gemini 2.5 Flash model responses when a US VIN has been included.\n",
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
   "execution_count": null,
   "id": "cf41e1a4-6eae-44dd-b4de-d628cade341e",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Install Gen AI\n",
    "!pip install --upgrade google-genai\n",
    "\n",
    "# Install Cloud Data Loss Prevention\n",
    "!pip install google-cloud-dlp --upgrade --user"
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
   "execution_count": null,
   "id": "f48dd97c-5ead-41e5-a006-0f8102171f03",
   "metadata": {
    "tags": []
   },
   "outputs": [],
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
   "execution_count": null,
   "id": "6cc70244-486b-4104-b9ca-74965fbcfff0",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Set project ID and region for location\n",
    "# You can find these details on the lab instruction page under Task 2\n",
    "PROJECT_ID = \"[your-project-id]\"  # @param {type:\"string\"}\n",
    "LOCATION = \"[your-region]\"  # @param {type:\"string\"}"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5063620e-85b3-4775-b8c0-cec8edaf2ae9",
   "metadata": {
    "tags": []
   },
   "source": [
    "### Import Gemini 2.5 Flash model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "771ffbb4-a600-468b-a143-59a7d88e5db3",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Create the API client\n",
    "from google import genai\n",
    "client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)\n",
    "model = \"gemini-2.5-flash\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2e5239cb-d8e1-4c2f-852c-a0ce3556c2ec",
   "metadata": {
    "tags": []
   },
   "source": [
    "## Update an existing Python function to block Gemini 2.5 Flash model responses when a US VIN has been included\n",
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
   "execution_count": null,
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
    "## Generate an example with VIN using Gemini 2.5 Flash model and block results\n",
    "\n",
    "In the code blocks below, generate an example text response containing a US Vehicle Identification Number (VIN) using the following prompt:\n",
    "\n",
    "`Is 4Y1SL65848Z411439 an example of a US Vehicle Identification Number (VIN)?`\n",
    "\n",
    "When generating the response, be sure to set the temperature to 0, so that the highest probability results are returned for the progress check below.\n",
    "\n",
    "Then, write and execute the appropriate code lines to block responses containing US Vehicle Identification Numbers (VIN)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb204161-0c3a-417c-b5f7-86b3b3e6b677",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Create prompt that generates an example response with US Vehicle Identification Number (VIN)\n",
    "# ADD YOUR CODE BELOW\n",
    "\n",
    "\n",
    "\n",
    "# Run model with prompt\n",
    "# Name the output as response_vin\n",
    "# ADD YOUR CODE BELOW\n",
    "\n",
    "\n",
    "\n",
    "# Print response without blocking it (VIN provided)\n",
    "# ADD YOUR CODE BELOW\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5dba6d7a-ad2b-495d-a05f-53ee63d07832",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Block model response that includes US Vehicle Identification Number (VIN)\n",
    "# ADD YOUR CODE BELOW\n"
   ]
  }
 ],
 "metadata": {
  "environment": {
   "kernel": "conda-base-py",
   "name": "workbench-notebooks.m128",
   "type": "gcloud",
   "uri": "us-docker.pkg.dev/deeplearning-platform-release/gcr.io/workbench-notebooks:m128"
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel) (Local) (Local)",
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
   "version": "3.10.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
