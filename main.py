#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import time

from pyppeteer import launch


async def main():
    browser = await launch(headless=False, executablePath="brave-browser")
    pageDigitalOcean = await browser.newPage()
    await pageDigitalOcean.goto('https://try.digitalocean.com/freetrialoffer/')
    time.sleep(2)
    await pageDigitalOcean.click("#lp-code-536 > form > div > div.signup-buttons > a.www-Button.www-Button--googleSSO.google-signup")
    time.sleep(3)
    await pageDigitalOcean.hover("#identifierId")
    await pageDigitalOcean.keyboard.type("7024cel@universidaddeleon.edu.mx")
    await pageDigitalOcean.keyboard.press("Enter")
    time.sleep(2)
    await pageDigitalOcean.keyboard.type("hola1808$")
    time.sleep(2)
    await pageDigitalOcean.keyboard.press("Enter")
    time.sleep(7)
    await pageDigitalOcean.keyboard.press("Tab")
    await pageDigitalOcean.keyboard.press("Enter")
    time.sleep(1000)




asyncio.run(main())
