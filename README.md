<div align="center">

<img src="docs/icons/logo.png" width="96" alt="MaplePal">

# MaplePal Field Guide

**A glass companion window that docks beside MapleStory.**<br>
Look anything up, get directions from where you stand, follow your quests, find where to train and see what your training is really earning, without alt-tabbing to a wiki.

<a href="https://github.com/gagandeepgill/maple-pal-public/releases/latest/download/MaplePal-Field-Guide-setup.exe"><img alt="Download for Windows (setup.exe)" src="docs/badges/download.svg" height="44"></a>

<a href="https://github.com/gagandeepgill/maple-pal-public/releases/latest"><img alt="Latest release" src="docs/badges/version.svg" height="28"></a>
<img alt="Windows 10 and 11, 64-bit" src="docs/badges/windows.svg" height="28">
<img alt="Updates itself" src="docs/badges/updates.svg" height="28">
<img alt="Beta" src="docs/badges/beta.svg" height="28">
<a href="https://www.virustotal.com/gui/file/cacf7b3e45acbc604db689402c7180df636ecb9a8657b9075b5432c725bc7669"><img alt="VirusTotal: every installer is scanned" src="docs/badges/virustotal.svg" height="28"></a>

🔒 **Every download ships a SHA-256 checksum and a signed GitHub build attestation** you can verify, and a separate window that never touches the game. <a href="#is-it-safe">Is it safe? →</a>

🧪 **This is a beta.** The Field Guide is new and changes often, so some things may not work yet or may break after a game patch. If something looks off, <a href="https://github.com/gagandeepgill/maple-pal-public/issues/new/choose">let us know</a>. Every report helps.

<br><br>

<img src="docs/hero.png" alt="The Field guide home, Directions, Training and Prices screens" width="100%">

</div>

## What it does

### <img src="docs/icons/field-guide.png" width="36" height="36" align="center" alt=""> Field guide
Search one catalog of mobs, maps, quests, items, NPCs, recipes, skills, shops, furniture and appearances. Press <kbd>Ctrl</kbd> <kbd>K</kbd> to search, then open a record to see its stats, drops, spawn maps and where to find it. Item pages also show the NPC sell price and which shops sell scarce potions. Everything is on your PC, so results show up as you type, and the library refreshes itself after a game patch.

### <img src="docs/icons/directions.png" width="36" height="36" align="center" alt=""> Directions from where you stand
Pick a destination, or one of the main towns and your recent trips, and the guide reads your minimap to find out where you are. It then draws the route on the real map art: which portal to take, when to climb, and when a taxi or town scroll is quicker. If your minimap is minimised or covered, it tells you so.

### <img src="docs/icons/quests.png" width="36" height="36" align="center" alt=""> Quest guide
<img src="docs/quests.png" alt="Quest guide card with accept, collect and turn-in steps, and the Quest accepted notice" width="420" align="right">

Each quest is laid out as **Accept → Collect → Turn in**, with the map, the monster and how far away it is. The guide reads your quest log and Etc inventory to know which step you're on. When you accept a quest at an NPC, a small **Quest accepted** notice shows its first step and fades after a few seconds. Click **Guide** to open its quest guide.

<br clear="right">

### <img src="docs/icons/training.png" width="36" height="36" align="center" alt=""> Training tracker
Start tracking and the widget reads your EXP bar: EXP per minute, your best minute, time to next level, and how this visit compares with your average. It also counts mesos and drops, the potions you used and their cost, and your kills (yours and your party's), and shows your net profit. It starts by itself once you're hunting, and reminds you when your inventory is full. Every visit is saved to **History**, grouped by day with that day's EXP.

**Where to train** suggests maps for your level and shows your own measured pace on maps you've trained on. Save your build (**I'm wearing this** on an equip's page fills it in). Thieves using Lucky Seven also get the maps ranked by estimated EXP per minute for that build, and more classes are on the way.

<p align="center"><img src="docs/where-to-train.png" alt="Where to train, ranked for a saved build" width="300">&nbsp;&nbsp;<img src="docs/history.png" alt="Training History grouped by day" width="300"></p>

### <img src="docs/icons/prices.png" width="36" height="36" align="center" alt=""> Prices
<img src="docs/price-watch.png" alt="Watched items with price targets" width="300" align="right">

Hover over an item in MapleStory and its price shows up in the widget: the last sale, median sale and median asking price, recent sales by channel, and how the price moved this week. Turn on **Watch price** on an item page, set a target, and the Prices tab tells you when it's reached. Prices come from Cozy Market and a shared price list.

<br clear="right">

### <img src="docs/icons/logo.png" width="36" height="36" align="center" alt=""> Made to sit beside the game
- **Dock** snaps it to the edge of the screen. When the game is full screen, it docks on your second monitor. **Focus** brings it forward when you return to the game, and MapleStory keeps your keyboard.
- **Open with MapleStory** starts the widget when the game comes to the front.
- Updates install in the background without a window over the game, and **What's new** lists what changed in each one.
- It reads only what the game already shows on screen and its installed files. It never changes the game or its files.

## Install

1. **[Download `MaplePal-Field-Guide-setup.exe`](https://github.com/gagandeepgill/maple-pal-public/releases/latest/download/MaplePal-Field-Guide-setup.exe)** and run it. It installs for your Windows user only, with no admin prompt, and adds a Start menu entry.
2. If Windows says **"Windows protected your PC"**, click **More info**, then **Run anyway**. This shows up because the installer isn't code-signed yet.
3. Open **MaplePal Field Guide** from the Start menu. The installer carries the whole library, so it sets itself up on the first start with nothing to download, even offline.
4. Play at any **UI Size**. The screen readers work with all of them, so keep the one you like.
5. If MapleStory isn't installed in `C:\Nexon\Library\maplestorycw`, for example if you play through Steam, open **Window settings → Open with MapleStory → Change** and choose its `MapleStory.exe`.

**Requirements:** 64-bit Windows 11, or Windows 10 version 2004 or later. If the PC doesn't have Microsoft Edge WebView2, the installer downloads it.

The release page also lists `MaplePal-Field-Guide-update.exe`. That's the smaller file the widget uses to update itself, without the library, so always install from `setup.exe`.

## Is it safe?

<table>
<tr><th>✅ What it does</th><th>🚫 What it never does</th></tr>
<tr><td valign="top">
<ul>
<li>Captures the MapleStory window, the way OBS or a screenshot tool does, to read the minimap, EXP bar and the item you hover over</li>
<li>Reads the game's installed files for maps, quests and items</li>
<li>Connects to GitHub for updates and new game data, to Cozy Market for prices, and to a data server for shared prices (and for the library, if GitHub can't be reached)</li>
<li>Saves its data in your own user folder</li>
</ul>
</td><td valign="top">
<ul>
<li>Draw on top of the game or hook into it — it's a separate window you dock beside MapleStory, <b>not an overlay</b></li>
<li>Read or change the game's memory, or inject anything into the game</li>
<li>Press keys or click for you (no botting or macros)</li>
<li>Ask for your Nexon or MapleStory login</li>
<li>Send your quests, Training history or settings anywhere</li>
</ul>
</td></tr>
</table>

**Check the download yourself**

- **Scan it:** upload the installer to [VirusTotal](https://www.virustotal.com), which runs it past about 70 antivirus engines. When a release's notes include a VirusTotal link, that scan was made by the same workflow that built the file.
- **Compare the checksum:** each release lists the installer's SHA-256 in its notes and in `SHA256SUMS.txt`. In PowerShell, run `Get-FileHash .\MaplePal-Field-Guide-setup.exe`. The hash should match exactly.
- **See where it was built:** every installer is built by this repository's public [Actions workflow](.github/workflows/release.yml), and the [build logs](https://github.com/gagandeepgill/maple-pal-public/actions) are public. Each build has a signed GitHub attestation. With the GitHub CLI, `gh attestation verify MaplePal-Field-Guide-setup.exe --repo gagandeepgill/maple-pal-public` confirms the file came from that workflow and wasn't changed after.
- **Updates are signed:** the widget installs an update only if it carries the release signature, so a tampered download is refused.

**Why does Windows warn about it?** SmartScreen shows "Windows protected your PC" for any new app that hasn't been code-signed and downloaded by many people yet. It isn't a virus detection. Click **More info**, then **Run anyway**.

## FAQ

<details>
<summary><b>Something isn't working. How do I report it?</b></summary>

Thanks for trying the beta! [Open a report](https://github.com/gagandeepgill/maple-pal-public/issues/new/choose) and say what you were doing, what you expected and what happened instead. Add the version from the bottom of the widget and a screenshot if you can. Please don't include your Nexon login or anything else private.
</details>

<details>
<summary><b>How does it update?</b></summary>

It checks for a new version every 30 minutes and downloads it in the background. The update installs when you click **Restart to update**, when you close the widget, or after 10 idle minutes when nothing is being tracked. Updates never show a window over the game, and **What's new** lists the changes afterwards. Every update is checked against a signature before it installs. After a game patch, the library updates itself too.
</details>

<details>
<summary><b>Is my data uploaded anywhere?</b></summary>

No. Your quest progress, Training history and settings stay on your PC in `%LOCALAPPDATA%\MaplePal\FieldGuide`. Updates and reinstalls never touch them. This repository holds only the installer and its update files. It has no source code and no player data.
</details>

<details>
<summary><b>Does it work for any character or server?</b></summary>

Yes. Nothing is tied to one character or account. Quest and Training progress builds up from whichever character you're playing on that PC.
</details>

<details>
<summary><b>Does it work on Mac?</b></summary>

Not directly. It's a Windows app, so on a Mac it needs a Windows virtual machine that can also run MapleStory.
</details>

<details>
<summary><b>The Training tracker or Prices show nothing.</b></summary>

Keep the MapleStory window visible, not minimised, with the EXP bar showing. Training reads the HUD, and Prices reads the item you're hovering over. If you play through Steam or installed the game outside `C:\Nexon\Library`, choose its `MapleStory.exe` in **Window settings → Open with MapleStory → Change**.
</details>

<details>
<summary><b>How do I uninstall it?</b></summary>

Uninstall **MaplePal Field Guide** from **Settings → Apps**. It also removes the **Open with MapleStory** sign-in watcher. Your data stays unless you tick **Delete the application data**.
</details>

---

<sub>MaplePal Field Guide is a fan-made tool and is not affiliated with or endorsed by Nexon. MapleStory is a trademark of Nexon.</sub>
