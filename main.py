{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNvm9x+ddtKXgGrRL7guTKr",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/alvarosp1/logocreator/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from fastapi import FastAPI\n",
        "from pydantic import BaseModel\n",
        "import requests\n",
        "import io\n",
        "from PIL import Image\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "app = FastAPI()\n",
        "\n",
        "API_URL = \"https://api-inference.huggingface.co/models/artificialguybr/LogoRedmond-LogoLoraForSDXL\"\n",
        "headers = {\"Authorization\": \"Bearer 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\"}\n",
        "\n",
        "class Item(BaseModel):\n",
        "    inputs: str\n",
        "\n",
        "@app.post(\"/query/\")\n",
        "async def create_query(item: Item):\n",
        "    response = requests.post(API_URL, headers=headers, json=item.dict())\n",
        "    image_bytes = response.content\n",
        "\n",
        "    image = Image.open(io.BytesIO(image_bytes))\n",
        "\n",
        "    fig, ax = plt.subplots()\n",
        "    ax.imshow(image)\n",
        "    ax.axis('off')\n",
        "    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)\n",
        "\n",
        "    plt.show()"
      ],
      "metadata": {
        "id": "fsz-wFpeEQle"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "uvicorn CreadorLogosFree:app --reload"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 140
        },
        "id": "JG5r-sy4E1Ej",
        "outputId": "ccaecd29-f783-43d8-b43f-5f40d102d0f5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-26-82fe6aed6c13>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    uvicorn CreadorLogosFree:app --reload\u001b[0m\n\u001b[0m            ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    }
  ]
}