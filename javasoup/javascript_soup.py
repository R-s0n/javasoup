import subprocess, os, sys

def install_on_kali():
    pip3_check = subprocess.run(["pip3 --version"], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, shell=True)
    if pip3_check.returncode == 0:
        print("[+] Pip3 is installed")
    else :
        print("[!] Pip3 is NOT installed -- Installing now...")
        subprocess.run(["sudo apt-get install -y python3-pip"], stdout=subprocess.DEVNULL, shell=True)
        print("[+] Pip3 was successfully installed")
    print("[-] Installing required packages...")
    subprocess.run(["pip3 install argparse bs4"], shell=True)
    node_check = subprocess.run(["node --version"], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, shell=True)
    if node_check.returncode == 0:
        print("[+] NodeJS is installed")
    else :
        print("[!] NodeJS is NOT installed -- Installing now...")
        subprocess.run(["sudo apt-get install -y nodejs npm"], stdout=subprocess.DEVNULL, shell=True)
        print("[+] NodeJS was successfully installed")
        node_check2 = subprocess.run(["node --version; npm --version"], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, shell=True)
        if node_check2.returncode == 0:
            print("[+] NodeJS was successfully installed")
        else:
            print("[-] Something went wrong!  Check the stack trace, make any necessary adjustments, and try again.  Exiting...")
            sys.exit(2)
    subprocess.run(["npm i puppeteer"], stdout=subprocess.DEVNULL, shell=True)
    print("[+] Installation complete!")

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