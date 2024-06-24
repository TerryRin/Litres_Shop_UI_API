import json
import logging

import allure
import requests
from allure_commons.types import AttachmentType


def litres_api_get(url, **kwargs):
    with allure.step("API Request"):
        response = requests.get(url="https://api.litres.ru" + url, **kwargs)
        allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json"),
        allure.attach(body=response.request.method + " " + response.request.url, name="Request",
                      attachment_type=AttachmentType.TEXT, extension="txt")
        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.text)
    return response


def litres_api_put(url, **kwargs):
    with allure.step("API Request"):
        response = requests.put(url="https://api.litres.ru" + url, **kwargs)
        allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json"),
        allure.attach(body=response.request.method + " " + response.request.url, name="Request",
                      attachment_type=AttachmentType.TEXT, extension="txt")
        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.text)
    return response


def litres_api_post(url, **kwargs):
    with allure.step("API Request"):
        response = requests.post(url="https://api.litres.ru" + url, **kwargs)
        allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json"),
        allure.attach(body=response.request.method + " " + response.request.url, name="Request",
                      attachment_type=AttachmentType.TEXT, extension="txt")
        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.text)
    return response


def litres_api_delete(url, **kwargs):
    with allure.step("API Request"):
        response = requests.delete(url="https://api.litres.ru" + url, **kwargs)
        allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json"),
        allure.attach(body=response.request.method + " " + response.request.url, name="Request",
                      attachment_type=AttachmentType.TEXT, extension="txt")
        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.text)
    return response
