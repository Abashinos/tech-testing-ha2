#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


class Settings(object):
    WEBDRIVER_TIMEOUT = 30
    WEBDRIVER_POLL_FREQUENCY = 0.1
    CHOSEN = u"Выбран"


class Credentials(object):
    TTHA2LOGIN = os.environ['TTHA2LOGIN']
    TTHA2PASSWORD = os.environ['TTHA2PASSWORD']
    DOMAIN = '@bk.ru'


class CampaignInfo(object):
    CAMPAIGN_NAME = "SnakeCampaign"
    BANNER_TITLE = "SnakeBanner"
    BANNER_TEXT = "Snake? SNAAAAAAAAAAAAAAAAKE"
    BANNER_URL = "snake.snake"
    BANNER_IMAGE = "/home/snake/Projects/tech-testing-ha2/tests/res/pic.jpg"
    INTERESTS = u"Компьютерная техника и программы"


class ElementsClasses(object):
    INTERESTS_TREE = "tree__wrapper"
    INTERESTS_INPUT = "tree__node__input"
    CHOSEN_BOX = "campaign-setting__chosen-box"
    CHOSEN_BOX_TEXT = "campaign-setting__chosen-box__item__name"
    CHOSEN_BOX_CLOSE = "campaign-setting__chosen-box__item__close"
    INCOME_DROPDOWN = "campaign-setting__value"
    INCOME_GROUPS = "campaign-setting__input"
    BANNER_PREVIEW = "banner-preview__img"
    BANNER_SUBMIT = "banner-form__save-button"
    SUBMIT_CAMPAIGN = "main-button-new"
    CAMPAIGN_TITLE = "campaign-title__name"
    BANNER_NAME = "banner-cell-name__name"
    BANNER_PREVIEW_TEXT = "banner-preview__text"
    BANNER_PREVIEW_IMG = "banner-preview__img"
    EDIT_BUTTON = "control__link_edit"
    CAMPAIGN_SETTING_VALUE = "campaign-setting__value"
    DELETE_BUTTON = "control__preset_delete"
    pass


class ElementsXPath(object):
    AD_LABEL = ".//label[text() = 'Внешний ресурс']"
    PAD_LABEL = ".//label[text() = 'Мой Мир: лента']"
    COMP_INTERESTS_DROPDOWN = "//span[@data-node-id='Компьютернаятехникаипрограммы']"
    COMP_INTERESTS_CHECKBOX = COMP_INTERESTS_DROPDOWN + "/../input[@class='tree__node__input']"
    CHOSEN_BOX = ".//span[text() = 'Компьютерная техника и программы']"
    BANNER_FORM_TITLE = ".//input[@data-name='title']"
    BANNER_FORM_TEXT = ".//textarea[@data-name='text']"
    BANNER_FORM_URL = ".//li[@data-top='false']//input[@data-name='url']"
    BANNER_FORM_IMAGE = ".//input[@data-name='image']"

    pass


class ElementsCSS(object):
    CAMPAIGN_NAME_FIELD = "[type='text']"
    INTERESTS_DROPDOWN = "[data-node-id='interests']"
    pass