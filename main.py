from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time as ti
import csv

jui=input()

if jui=="https://prposting.com":
    with open("prposting.csv", "w", newline='',encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(
            ["domen", "them", "dr", "trafik","price"]
        )
    c = "iou"
    domen = []
    them = []
    dr = []
    trafik = []
    price=[]
    y = 1
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://prposting.com")
    f = input()
    while y < 2:
        ti.sleep(7)
        t = driver.find_elements_by_css_selector("a.is-size-6")
        t2 = driver.find_elements_by_css_selector("td:nth-of-type(1) tr:nth-of-type(2) td")
        t3 = driver.find_elements_by_css_selector("td:nth-of-type(2) .has-text-right span")
        t4 = driver.find_elements_by_css_selector("td:nth-of-type(2) tr:nth-of-type(2) td.has-text-right")
        t5 = driver.find_elements_by_css_selector("div.field:nth-of-type(1) .field .is-primary span:nth-of-type(2)")
        if t==c:
            y=2
        else:
            for i in range(0, len(t)):
                domen.append(t[i].text)
            for i in range(0, len(t2)):
                them.append(t2[i].text)
            for i in range(0, len(t3)):
                dr.append(t3[i].text)
            for i in range(0, len(t4)):
                trafik.append(t4[i].text)
            for i in range(0, len(t5)):
                price.append(t5[i].text.replace(" ","").replace(",",".").replace("₴",""))
            ti.sleep(7)
        c=t
        try:
           next = "a.pagination-next.is-hidden-mobile"
           o = driver.find_element_by_css_selector(next).click()
        except Exception as _ex:
            y = 2
    print(len(domen))
    print(len(them))
    print(len(dr))
    print(len(trafik))
    print(len(price))
    assert len(domen) == len(them) == len(dr)==len(trafik)==len(price)
    for i in range(0, len(domen)):
        with open("prposting.csv", "a", newline='',encoding="utf-8-sig") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                [domen[i], them[i], dr[i], trafik[i],price[i]]
            )



if jui=="https://links-stream.ru":
    with open("links-stream.csv", "w", newline='',encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(
            ["domen", "them", "dr", "region","price1","price2"]
        )
    c = "iou"
    domen = []
    them = []
    dr=[]
    region=[]
    price1 = []
    price2 = []
    y = 1
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://links-stream.ru")
    f = input()
    ti.sleep(7)
    t = driver.find_elements_by_css_selector("a.domain_link")
    t2 = driver.find_elements_by_css_selector(".line2 div.sub_line2")
    t3 = driver.find_elements_by_css_selector("div.td:nth-of-type(3) div.line3")
    t31 = driver.find_elements_by_css_selector("div.td:nth-of-type(8) thead td:nth-of-type(1)")
    t4 = driver.find_elements_by_css_selector(".text_wrap div.sub_line1")
    t5 = driver.find_elements_by_css_selector(".ls_site div:nth-of-type(9)")
    for i in range(0, len(t)):
        domen.append(t[i].text)
    for i in range(0, len(t2)):
        them.append(t2[i].text)
    for i in range(0, len(t3)):
        dr.append(t3[i].text)
    for i in range(0, len(t31)):
        region.append(t31[i].text)
    for i in range(0, len(t4)):
        price1.append(t4[i].text)
    for i in range(0, len(t5)):
        h = t5[i].text.replace("Статья:", "").replace("В КОРЗИНУ", "").replace(" ", "").replace("\n", "").replace("₴"," ").split()
        if len(h) == 2:
            r = float(h[0]) + float(h[1])
        else:
            r = float(h[0])
        price2.append(r)
    ti.sleep(7)
    try:
       next = "/html/body/main/section[2]/div/div[2]/div[1]/div/a[2]"
       o = driver.find_element_by_xpath(next).click()
    except Exception as _ex:
        y = 2
    if y!=2:
        ti.sleep(7)
        t = driver.find_elements_by_css_selector("a.domain_link")
        t2 = driver.find_elements_by_css_selector(".line2 div.sub_line2")
        t3 = driver.find_elements_by_css_selector("div.td:nth-of-type(3) div.line3")
        t31 = driver.find_elements_by_css_selector("div.td:nth-of-type(8) thead td:nth-of-type(1)")
        t4 = driver.find_elements_by_css_selector(".text_wrap div.sub_line1")
        t5 = driver.find_elements_by_css_selector(".ls_site div:nth-of-type(9)")
        for i in range(0, len(t)):
            domen.append(t[i].text)
        for i in range(0, len(t2)):
            them.append(t2[i].text)
        for i in range(0, len(t3)):
            dr.append(t3[i].text)
        for i in range(0, len(t31)):
            region.append(t31[i].text)
        for i in range(0, len(t4)):
            price1.append(t4[i].text)
        for i in range(0, len(t5)):
            h = t5[i].text.replace("Статья:", "").replace("В КОРЗИНУ", "").replace(" ", "").replace("\n", "").replace(
                "₴", " ").split()
            if len(h) == 2:
                r = float(h[0]) + float(h[1])
            else:
                r = float(h[0])
            price2.append(r)
        ti.sleep(7)
    try:
       next = "/html/body/main/section[2]/div/div[2]/div[1]/div/a[4]"
       o = driver.find_element_by_xpath(next).click()
    except Exception as _ex:
        y = 2
    if y!=2:
        ti.sleep(7)
        t = driver.find_elements_by_css_selector("a.domain_link")
        t2 = driver.find_elements_by_css_selector(".line2 div.sub_line2")
        t3 = driver.find_elements_by_css_selector("div.td:nth-of-type(3) div.line3")
        t31 = driver.find_elements_by_css_selector("div.td:nth-of-type(8) thead td:nth-of-type(1)")
        t4 = driver.find_elements_by_css_selector(".text_wrap div.sub_line1")
        t5 = driver.find_elements_by_css_selector(".ls_site div:nth-of-type(9)")
        for i in range(0, len(t)):
            domen.append(t[i].text)
        for i in range(0, len(t2)):
            them.append(t2[i].text)
        for i in range(0, len(t3)):
            dr.append(t3[i].text)
        for i in range(0, len(t31)):
            region.append(t31[i].text)
        for i in range(0, len(t4)):
            price1.append(t4[i].text)
        for i in range(0, len(t5)):
            h = t5[i].text.replace("Статья:", "").replace("В КОРЗИНУ", "").replace(" ", "").replace("\n", "").replace(
                "₴", " ").split()
            if len(h) == 2:
                r = float(h[0]) + float(h[1])
            else:
                r = float(h[0])
            price2.append(r)
        ti.sleep(7)
    try:
       next = "/html/body/main/section[2]/div/div[2]/div[1]/div/a[5]"
       o = driver.find_element_by_xpath(next).click()
    except Exception as _ex:
        y = 2
    if y!=2:
        ti.sleep(7)
        t = driver.find_elements_by_css_selector("a.domain_link")
        t2 = driver.find_elements_by_css_selector(".line2 div.sub_line2")
        t3 = driver.find_elements_by_css_selector("div.td:nth-of-type(3) div.line3")
        t31 = driver.find_elements_by_css_selector("div.td:nth-of-type(8) thead td:nth-of-type(1)")
        t4 = driver.find_elements_by_css_selector(".text_wrap div.sub_line1")
        t5 = driver.find_elements_by_css_selector(".ls_site div:nth-of-type(9)")
        for i in range(0, len(t)):
            domen.append(t[i].text)
        for i in range(0, len(t2)):
            them.append(t2[i].text)
        for i in range(0, len(t3)):
            dr.append(t3[i].text)
        for i in range(0, len(t31)):
            region.append(t31[i].text)
        for i in range(0, len(t4)):
            price1.append(t4[i].text)
        for i in range(0, len(t5)):
            h = t5[i].text.replace("Статья:", "").replace("В КОРЗИНУ", "").replace(" ", "").replace("\n", "").replace(
                "₴", " ").split()
            if len(h) == 2:
                r = float(h[0]) + float(h[1])
            else:
                r = float(h[0])
            price2.append(r)
        ti.sleep(7)
    try:
       next = "/html/body/main/section[2]/div/div[2]/div[1]/div/a[6]"
       o = driver.find_element_by_xpath(next).click()
    except Exception as _ex:
        y = 2
    if y!=2:
        ti.sleep(7)
        t = driver.find_elements_by_css_selector("a.domain_link")
        t2 = driver.find_elements_by_css_selector(".line2 div.sub_line2")
        t3 = driver.find_elements_by_css_selector("div.td:nth-of-type(3) div.line3")
        t31 = driver.find_elements_by_css_selector("div.td:nth-of-type(8) thead td:nth-of-type(1)")
        t4 = driver.find_elements_by_css_selector(".text_wrap div.sub_line1")
        t5 = driver.find_elements_by_css_selector(".ls_site div:nth-of-type(9)")
        for i in range(0, len(t)):
            domen.append(t[i].text)
        for i in range(0, len(t2)):
            them.append(t2[i].text)
        for i in range(0, len(t3)):
            dr.append(t3[i].text)
        for i in range(0, len(t31)):
            region.append(t31[i].text)
        for i in range(0, len(t4)):
            price1.append(t4[i].text)
        for i in range(0, len(t5)):
            h = t5[i].text.replace("Статья:", "").replace("В КОРЗИНУ", "").replace(" ", "").replace("\n", "").replace(
                "₴", " ").split()
            if len(h) == 2:
                r = float(h[0]) + float(h[1])
            else:
                r = float(h[0])
            price2.append(r)
        ti.sleep(7)
    while y < 2:
        ti.sleep(7)
        t = driver.find_elements_by_css_selector("a.domain_link")
        t2 = driver.find_elements_by_css_selector(".line2 div.sub_line2")
        t3 = driver.find_elements_by_css_selector("div.td:nth-of-type(3) div.line3")
        t31=driver.find_elements_by_css_selector("div.td:nth-of-type(8) thead td:nth-of-type(1)")
        t4 = driver.find_elements_by_css_selector(".text_wrap div.sub_line1")
        t5 = driver.find_elements_by_css_selector(".ls_site div:nth-of-type(9)")
        for i in range(0, len(t)):
            domen.append(t[i].text)
        for i in range(0, len(t2)):
            them.append(t2[i].text)
        for i in range(0, len(t3)):
            dr.append(t3[i].text)
        for i in range(0, len(t31)):
            region.append(t31[i].text)
        for i in range(0, len(t4)):
            price1.append(t4[i].text)
        for i in range(0, len(t5)):
            h = t5[i].text.replace("Статья:", "").replace("В КОРЗИНУ", "").replace(" ", "").replace("\n", "").replace(
                "₴", " ").split()
            if len(h) == 2:
                r = float(h[0]) + float(h[1])
            else:
                r = float(h[0])
            price2.append(r)
        ti.sleep(7)
        try:
           next="/html/body/main/section[2]/div/div[2]/div[1]/div/a[7]"
           o = driver.find_element_by_xpath(next).click()
        except Exception as _ex:
            y=2
    assert len(domen) == len(them) == len(price1)==len(dr)==len(region)==len(price2)
    for i in range(0, len(domen)):
        with open("links-stream.csv", "a", newline='',encoding="utf-8-sig") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                [domen[i], them[i], dr[i],region[i],price1[i], price2[i]]
            )


if jui=="https://www.miralinks.ru":
    with open("mrlinks.csv", "w", newline='',encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(
            ["domen", "them", "price1", "price2"]
        )
    c = "iou"
    domen = []
    them = []
    price1 = []
    price2 = []
    y = 1
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.miralinks.ru")
    f = input()
    while y < 2:
        ti.sleep(7)
        t = driver.find_elements_by_css_selector("a.popover-holder")
        t2 = driver.find_elements_by_css_selector("td:nth-of-type(15)")
        t3 = driver.find_elements_by_css_selector(".rPos .nowrap span.RUR")
        t4 = driver.find_elements_by_css_selector(".rPos > span.RUR")
        if t == c:
            y = 2
        else:
            for i in range(0, len(t)):
                domen.append(t[i].text)
            for i in range(0, len(t2)):
                them.append(t2[i].text)
            for i in range(0, len(t3)):
                price1.append(t3[i].text)
            for i in range(0, len(t4)):
                price2.append(str(float(t3[i].text.replace(" ", "")) + float(t4[i].text.replace(" ", ""))))
        c = t
        ti.sleep(7)
        next = "Catalog_50522879_next_pg_35"
        o = driver.find_element_by_id(next).click()
    assert len(domen) == len(them) == len(price1)
    for i in range(0, len(domen)):
        with open("mrlinks.csv", "a", newline='',encoding="utf-8-sig") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                [domen[i], them[i], price1[i], price2[i]]
            )

elif jui=="https://collaborator.pro":
    with open("coloborator.csv", "w", newline='',encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(
            ["domen", "them", "dr", "trafik", "price1", "price2"]
        )
    c = "iou"
    domen = []
    them = []
    dr = []
    trafik = []
    price1 = []
    price2 = []
    y = 1
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://collaborator.pro")
    f = input()
    while y < 2:
        ti.sleep(7)
        t = driver.find_elements_by_class_name("link_ellipsis")
        t2 = driver.find_elements_by_class_name("c-t-theme")
        t3 = driver.find_elements_by_css_selector(".format-item--article div.creator-price__publication-value")
        t4 = driver.find_elements_by_css_selector("div.format-item--article")
        t5 = driver.find_elements_by_css_selector("td:nth-of-type(7)")
        t6 = driver.find_elements_by_css_selector("td:nth-of-type(6)")
        if t == c:
            y = 2
        else:
            for i in range(0, len(t)):
                domen.append(t[i].text)
            for i in range(0, len(t2)):
                them.append(t2[i].text)
            for i in range(0, len(t6)):
                dr.append(t6[i].text)
            for i in range(0, len(t5)):
                trafik.append(t5[i].text)
            for i in range(0, len(t3)):
                price1.append(t3[i].text)
            for i in range(0, len(t4)):
                h = t4[i].text.replace("Статья", "").replace("\n", "").replace("грн", "").split()
                if len(h) == 2:
                    r = float(h[0]) + float(h[1].replace("+", ""))
                else:
                    r = float(h[0])
                price2.append(r)
        c = t
        ti.sleep(7)
        xpath = "/html/body/div[1]/div[1]/div[2]/div[4]/div[2]/div/div[3]/div[2]/div[1]/nav/ul/li[9]/a"
        o = driver.find_element_by_xpath(xpath).click()
    assert len(domen) == len(them) == len(dr) == len(trafik) == len(price1) == len(price2)
    for i in range(0, len(domen)):
        with open("coloborator.csv", "a", newline='',encoding="utf-8-sig") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                [domen[i], them[i], dr[i], trafik[i], price1[i], price2[i]]
            )
elif jui=="https://gogetlinks.net":
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import time as ti
    import csv

    name_1 = "Links"
    name_2 = "price"

    with open("gogetlinks.csv", "w", newline='',encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(
            [name_1, name_2]
        )

    u = []
    r = []
    y = 1
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://gogetlinks.net/")
    f = input()
    t = driver.find_elements_by_class_name("site-link__info")
    t2 = driver.find_elements_by_class_name("white-space_nowrap")
    for i in range(0, len(t)):
        u.append(t[i].text)
    for i in range(0, len(t2)):
        r.append(t2[i].text)
    ti.sleep(3)
    xpath = "/html/body/div[1]/div[2]/div/div[4]/div[2]/div[2]/div[4]/div/a[1]"
    o = driver.find_element_by_xpath(xpath).click()
    ti.sleep(3)
    t = driver.find_elements_by_class_name("site-link__info")
    t2 = driver.find_elements_by_class_name("white-space_nowrap")
    for i in range(0, len(t)):
        u.append(t[i].text)
    for i in range(0, len(t2)):
        r.append(t2[i].text)
    ti.sleep(3)
    xpath = "/html/body/div[1]/div[2]/div/div[4]/div[2]/div[2]/div[4]/div/a[2]"
    o = driver.find_element_by_xpath(xpath).click()
    ti.sleep(3)
    t = driver.find_elements_by_class_name("site-link__info")
    t2 = driver.find_elements_by_class_name("white-space_nowrap")
    for i in range(0, len(t)):
        u.append(t[i].text)
    for i in range(0, len(t2)):
        r.append(t2[i].text)
    ti.sleep(3)
    xpath = "/html/body/div[1]/div[2]/div/div[4]/div[2]/div[2]/div[4]/div/a[3]"
    o = driver.find_element_by_xpath(xpath).click()
    ti.sleep(3)
    t = driver.find_elements_by_class_name("site-link__info")
    t2 = driver.find_elements_by_class_name("white-space_nowrap")
    for i in range(0, len(t)):
        u.append(t[i].text)
    for i in range(0, len(t2)):
        r.append(t2[i].text)
    ti.sleep(3)
    while y < 2:
        try:
            xpath = "/html/body/div[1]/div[2]/div/div[4]/div[2]/div[2]/div[4]/div/a[4]"
            o = driver.find_element_by_xpath(xpath).click()
            ti.sleep(10)
            t = driver.find_elements_by_class_name("site-link__info")
            t2 = driver.find_elements_by_class_name("white-space_nowrap")
            for i in range(0, len(t)):
                u.append(t[i].text)
            for i in range(0, len(t2)):
                r.append(t2[i].text)
            ti.sleep(10)
        except Exception as _ex:
            xpath = "/html/body/div[1]/div[2]/div/div[4]/div[2]/div[2]/div[4]/div/a[3]"
            o = driver.find_element_by_xpath(xpath).click()
            ti.sleep(10)
            t = driver.find_elements_by_class_name("site-link__info")
            t2 = driver.find_elements_by_class_name("white-space_nowrap")
            for i in range(0, len(t)):
                u.append(t[i].text)
            for i in range(0, len(t2)):
                r.append(t2[i].text)
            y = 2
    assert len(r) == len(u)
    for i in range(0, len(u)):
        with open("gogetlinks.csv", "a", newline='',encoding="utf-8-sig") as csvfile:
            writer = csv.writer(csvfile, delimiter=";")
            writer.writerow(
                [u[i], r[i]]
            )
