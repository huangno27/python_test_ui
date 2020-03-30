class Objectpage_datas_jijian:
    index_loc = '//a[text()="登录"]'
    dl_anniu = '//span[text()="密码登录"]'
    user_loc = '//input[@name="tel"]'
    password_loc = '//input[@name="pwd"]'
    yzm_loc = '//input[@name="gvcvalue"]'
    login_button_loc = '/html/body/modal-container/div/div/app-registered-login/div/div[3]/form/button'

    jj_loc = '//li[@class="col-xs-2"]/child::a'

    yy_qujian = '//ul[@class="index_nav_menu"]/child::li[2]/child::span'
    ydh_srk = '//input[@class="data-input"]'
    ydh_cxan = '//button[contains(@class,btn_red)]'

    yfsx_anniu = '//span[text()="运费/时效"]'
    contory_an = '//input[contains(@name,"receiverCountryName")]'
    fj_city_an = '//input[contains(@name,"sendercity")]'
    fj_address_an = '//input[contains(@name,"senderZip")]'

    sj_city_an = '//input[contains(@name,"recevierCity")]'
    sj_address_an = '//input[contains(@name,"recevierZipCode")]'
    sbjz_an = '//input[contains(@name,"declaredValueName")]'
    js_an = '//select[contains(@name,"expressNumName")]'
    kj_zl_an = '//input[contains(@name,"weight")]'
    kj_chang_an = '//input[contains(@name,"length")]'
    kj_kuan_an = '//input[contains(@name,"width")]'
    kj_gao_an = '//input[contains(@name,"height")]'

    # 包裹/文件按钮
    bg_an = '//*[@id="detail"]/div[2]/input[1]'
    wj_an = '/html/body/app-root/div[2]/app-fee/div/div[2]/form/div[3]/div[2]/input[2]'
    zlxz_an = '//select[contains(@name,"fileWeightName")]'
    # 最下的3个按钮
    qk_an = '//button[contains(@class,"btn_clear")]'
    cxyfsx_an = '//button[contains(@class,"btn_red disabled-btn")]'
    sxzh_an = '//button[contains(@class,"btn_red disabled-btn")]'

    # 退出
    qt_an = '//a[contains(@class,"registered-a")]'