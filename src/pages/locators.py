
class MainPageLocators:
    """ Main Page elements"""
    all_menu_buttons = '//p[string-length(text()) > 4]' # iterable
    en_menu_button_xpath = '//*[@id="element_464_content"]'
    de_menu_button_xpath = '//*[@id="element_463_content"]'
    fr_menu_button_xpath = '//*[@id="element_468_content"]'
    pl_menu_button_xpath = '//*[@id="element_473_content"]'

    kandelo_logo = '//*[@id="element_738_image"]'
    care_logo = '//*[@id="element_1496_image"]'
    main_slider_xpath = '//*[@itemprop="image"]'
    mail_address_xpath = '//*[@class="custom_link"]'


class HeaderLocators:
    """ Pages header elements """
    logo_xpath = '//*[@id="element_981_image"]'
    homepage_button_xpath = '//*[@id="element_982_content"]/div[2]/nav/ol/li[1]/a/span'
    our_candles_button_xpath = '//a[@pageid="webpage_22"]'
    make_candle_button_xpath = '//a[@pageid="webpage_23"]'
    where_to_buy_button_xpath = '//a[@pageid="webpage_28"]'
    faq_button_xpath = '//a[@pageid="webpage_24"]'
    contact_button_xpath = '//*[@class="ww_menu_item_link ww_element_982_menu_level0"]/span[contains(text(), ' \
                           '"Contact")] '

