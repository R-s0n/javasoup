import subprocess, os

def get_soup(url):
    cwd = os.getcwd()
    javasoup_js = """const puppeteer = require('puppeteer');

function getHtml(url){
    try {
        (async () => {
            const browser = await puppeteer.launch();
            const page = await browser.newPage();
            try {
                await page.goto(url, {
                    waitUntil: 'networkidle0'
                });
            } catch (error) {
                console.log(error);
                process.exit(1);
            }
            try {
                const data = await page.content();
                console.log(data);
            } catch (error) {
                console.log(error);
                process.exit(1);
            }

            try {
                await browser.close();
            } catch (error) {
                console.log(error);
                process.exit(1);
            }
        })();
    } catch (error) {
        console.log(error);
        process.exit(1);
    }
}

getHtml(process.argv[2]);"""
    f = open(f'{cwd}/javasoup.js', 'w')
    f.write(javasoup_js)
    f.close()
    get_content = subprocess.run([f'node javasoup.js {url}'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, shell=True)
    subprocess.run([f"rm {cwd}/javasoup.js"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, text=True, shell=True)
    return get_content.stdout