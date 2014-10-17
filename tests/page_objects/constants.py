#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Settings(object):
    WEBDRIVER_TIMEOUT = 30
    WEBDRIVER_POLL_FREQUENCY = 0.1


class Credentials(object):
    TTHA2LOGIN = 'tech-testing-ha2-1'
    TTHA2PASSWORD = 'Pa$$w0rD-1'
    DOMAIN = '@bk.ru'


class CampaignInfo(object):
    CAMPAIGN_NAME = "SnakeCampaign"
    BANNER_TITLE = "SnakeBanner"
    BANNER_TEXT = "Snake? SNAAAAAAAAAAAAAAAAKE"
    BANNER_URL = "snake.snake"
    BANNER_IMAGE = "/home/snake/Projects/tech-testing-ha2/tests/res/pic.jpg"


class ElementsClasses(object):
    INTERESTS_TREE = "tree__wrapper"
    INTERESTS_INPUT = "tree__node__input"
    CHOSEN_BOX = "campaign-setting__chosen-box"
    CHOSEN_BOX_CLOSE = "campaign-setting__chosen-box__item__close"
    INCOME_DROPDOWN = "campaign-setting__value"
    INCOME_GROUPS = "campaign-setting__input"
    BANNER_PREVIEW = "banner-preview__img"
    BANNER_SUBMIT = "banner-form__save-button"
    pass


class ElementsXPath(object):
    PAD_CHOICE = ".//input[@data-name='external_feed_abstract']"
    COMP_INTERESTS_DROPDOWN = "//span[@data-node-id='Компьютернаятехникаипрограммы']"
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