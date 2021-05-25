class MainPageLocators:
    """ Main Page elements"""
    all_menu_buttons = '//p[string-length(text()) > 4]'  # iterable
    en_menu_button_xpath = '//*[@id="element_464_content"]'
    de_menu_button_xpath = '//*[@id="element_463_content"]'
    fr_menu_button_xpath = '//*[@id="element_468_content"]'
    pl_menu_button_xpath = '//*[@id="element_473_content"]'

    kandelo_logo = '//*[@id="element_738_image"]'
    care_logo = '//*[@id="element_1496_image"]'
    main_slider_xpath = '//*[@itemprop="image"]'
    mail_address_xpath = '//*[@class="custom_link"]'


class HeaderLocators:
    """ Pages header menu elements """
    logo_xpath = '//*[@id="element_981_image"]'
    homepage_button_xpath = '//*[@id="element_982_content"]/div[2]/nav/ol/li[1]/a/span'
    our_candles_button_xpath = '//a[@pageid="webpage_22"]'
    make_candle_button_xpath = '//a[@pageid="webpage_23"]'
    where_to_buy_button_xpath = '//a[@pageid="webpage_28"]'
    faq_button_xpath = '//a[@pageid="webpage_24"]'
    contact_button_xpath = '//*[@class="ww_menu_item_link ww_element_982_menu_level0"]/span[contains(text(), ' \
                           '"Contact")] '


class HomePageLocators:
    """ Home Page elements """
    h1_titles_xpath = '//*[h1]'
    email_input_xpath = '//*[@id="element_1042_form"]/table/tbody/tr[1]/td[2]/div/label/input'
    contact_text_field_xpath = '//*[@id="element_1042_form"]/table/tbody/tr[2]/td[2]/div/label/textarea'
    send_form_button_xpath = '//*[@class="ww_inner_element_content ww_submit_button_content"]'
    error_message_xpath = '//*[@class="ww_inner_element_content ww_form_frame_info_error p_default_block"]'
    sent_message_xpath = '//*[@class="ww_inner_element_content ww_form_frame_info p_default_block"]'
    sample_email = 'jdoe@oops.op'
    sample_message = 'This is sample message'


class ProductsPageLocators:
    """ Products Page elements """
    products_titles_xpath = '//*[h1]'
    top_products_list_xpath = '//*[contains(@groupid, "group_62")]' # minus 2 lines and -2 headers in the group
    products_gallery_xpath = '//*[@class="gv_gallery" and contains(@style, "530px")]'
    weight_field_xpath = '//*[contains(strong, "Weight")]'
    dimensions_field_xpath = '//*[contains(strong, "Dimensions")]'
