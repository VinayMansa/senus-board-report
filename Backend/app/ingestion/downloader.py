import json
import os
import requests

CONFIG_PATH = "app/config/report_sources.json"
DOWNLOAD_FOLDER = "uploads/reports"

os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


def download_report(url: str):

    filename = url.split("/")[-1]

    save_path = os.path.join(
        DOWNLOAD_FOLDER,
        filename,
    )

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Failed to download report")

    with open(save_path, "wb") as pdf:
        pdf.write(response.content)

    return filename, save_path

    with open(CONFIG_PATH, "r") as file:
        reports = json.load(file)

    downloaded_reports = []

    for report in reports:

        url = report["url"]

        filename = url.split("/")[-1]

        save_path = os.path.join(
            DOWNLOAD_FOLDER,
            filename,
        )

        response = requests.get(url)

        if response.status_code == 200:

            with open(save_path, "wb") as pdf:

                pdf.write(response.content)

            report["local_path"] = save_path

            downloaded_reports.append(report)

    return downloaded_reports