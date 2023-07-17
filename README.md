<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![Twitter][twitter-shield]][twitter-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/keyooner/botnet">
    <img src="ReadmeImages/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Twitter Botnet</h3>

  <p align="center">
    An amazing app to create influence on Twitter!
    <br />
    <a href="https://github.com/keyooner/botnet"><strong>Explore documentation »</strong></a>
    <br />
    <br />
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#issues">Issues</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Botnet Twitter Welcome Screenshot][botnet-screenshot-light]](https://example.com)
[![Botnet Twitter Welcome Screenshot][botnet-screenshot-dark]](https://example.com)

This app it was created as an easy way to crate fake influence on Twitter. It's easy to use and have many fantastics automated options. Also, you can choose between dark themes or light themes in the gui app.

Automated options:
* Create twitter users
* Give likes
* Give retweets
* Give follows

All this actions could be realised using a nord-vpn connection or not, you must choose. If you want to use it, you neede it a nord-vpn account.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This app it was created using:

* VisualStudio Code
* Python
* Selenium
* Firebase
* Cryptography
* CustomTkinter

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Easy way to use:

* Download the project as a zip or clone the repository 

* Run the project using VisualStudio Code or similar workspace.

### Prerequisites 

* Accounts: CPanel account to using the API to asociate the Twitter accounts and Firebase.
* Software: VisualStudio Code or similar and Python
* Frameworks: Firebase, Selenium, Cryptography, CustomTkinter, CTKTable, Faker, Firebase, IMAP Tools, NordVPN Switcher, Pillow and WebDriver Manager, 
* Optional: Nord-VPN account


### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a API Key at [https://cpanel.net](https://cpanel.net)
2. Clone or download the repository
   ```sh
   git clone https://github.com/keyooner/botnet.git
   ```
3. Install PIP packages
   ```sh
   pip install cryptography
   pip install customtkinter
   pip install CTkTable
   pip install Faker
   pip install firebase-admin
   pip install imap-tools
   pip install nordvpn-switcher
   pip install Pillow
   pip install Selenium
   pip install webdriver-manager
   ```
4. Enter your CPanel API and Firebase info in `const.py`
   _Cpanel
   ```sh
   CPANEL_API_TOKEN = "your_API_token"
   CPANEL_BASE_URL = "https://your_domain_.com:your_port/"
   CPANEL_USERNAME = "your_username"
   IMAP_SERVER = "mail.raptoragency.es"
   DOMINIO = "your_domain_.com"
   ```
   Firebase
   ```sh
   CONFIG = {
        "apiKey": "AIzaSyAPBY89KNnKBP0fYyAPUf-u5M7EyPc3u_U",
        "authDomain": "tfm-bbdd-2f16f.firebaseapp.com",
        "databaseURL": "https://tfm-bbdd-2f16f-default-rtdb.europe-west1.firebasedatabase.app",
        "projectId": "tfm-bbdd-2f16f",
        "storageBucket": "tfm-bbdd-2f16f.appspot.com",
        "messagingSenderId": "830225056723",
        "appId": "1:830225056723:web:39aef3e2cdf9efd33d6526",
        "measurementId": "G-TGCX8QGXRY"
     }
   ```
6. Run the project and enjoy it 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- BUGS -->
## Issues
VisualStudioCode can't import modules

Solution: Ctrl + Shift + P -> Go to User.settings.json -> Add de following line:
```sh
"terminal.integrated.env.windows": { "PYTHONPATH": "${workspaceFolder}" }
```

<!-- USAGE EXAMPLES -->
## Usage

Run the project and create or unlock accounts before do twitter actions.

[![Twitter Actions Screenshot][twitter-actions-screenshot-light]](https://github.com/keyooner/botnet)
[![Twitter Actions Screenshot][twitter-actions-screenshot-dark]](https://github.com/keyooner/botnet)

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License
Created by us without restrctions.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

* Cristian Agredano Momblan - [@tfm_botnet](https://twitter.com/tfm_botnet)
* Daniel Fernández Lozano - [@tfm_botnet](https://twitter.com/tfm_botnet)

Project Link: [https://github.com/keyooner/botnet](https://github.com/keyooner/botnet)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/keyooner/botnet/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/keyooner/botnet/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/keyooner/botnet/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/keyooner/botnet/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/keyooner/botnet/blob/master/LICENSE.txt
[twitter-shield]: https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white
[twitter-url]: https://twitter.com/tfm_botnet
[botnet-screenshot-light]: ReadmeImages/screenshot_light.png
[botnet-screenshot-dark]: ReadmeImages/screenshot_dark.png
[twitter-actions-screenshot-light]: ReadmeImages/twitter_actions_light.png
[twitter-actions-screenshot-dark]: ReadmeImages/twitter_actions_dark.png
