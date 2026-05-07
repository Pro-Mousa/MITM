<!-- Banner -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=200&color=0:1F1C2C,100:928DAB&section=header&text=ARP%20MITM%20Tool&fontSize=50&fontColor=ffffff&desc=Python%20Scapy%20Tool&descSize=22&descAlignY=65&descColor=ffffff" alt="header" />
</p>

<p align="center">
  <b>🛡️ ARP MITM Tool (Python + Scapy)</b><br>
  <i>A simple Python script for ARP spoofing and Man-in-the-Middle (MITM) network demonstrations.</i>
</p>

---

<h2>📌 Features</h2>

<ul>
  <li>Performs ARP spoofing between target and gateway</li>
  <li>Automatically retrieves MAC addresses</li>
  <li>Continuous ARP poisoning attack loop</li>
  <li>Restores ARP tables automatically after exit</li>
  <li>Simple command-line interface</li>
</ul>

---

<h2>⚙️ Requirements</h2>

<ul>
  <li>Python 3</li>
  <li>Linux-based OS</li>
  <li>Scapy library</li>
  <li>Root/sudo privileges</li>
  <li>Devices connected to the same local network</li>
</ul>

---

<h2>📥 Installation</h2>

<p>Clone the repository:</p>

<pre>
git clone https://github.com/your-username/MITM.git
cd MITM
</pre>

<p>Install dependencies:</p>

<pre>
pip install scapy
</pre>

or

<pre>
pip install -r requirements.txt
</pre>

---

<h2>🚀 Usage</h2>

<p>⚠️ Run the script with sudo/root privileges</p>

<h3>Using Python 3</h3>

<pre>
sudo python3 arp_poison.py -t &lt;target_ip&gt; -g &lt;gateway_ip&gt;

or

sudo python3 arp_poison.py --target &lt;target_ip&gt; --gateway &lt;gateway_ip&gt;
</pre>
---

<h2>🧪 Example</h2>

<pre>
sudo python3 arp_poison.py -t 192.168.1.3 -g 192.168.1.1
</pre>

---

<h2>🧠 How It Works</h2>

<ul>
  <li>Gets target and gateway IP addresses from user input</li>
  <li>Sends ARP requests to discover MAC addresses</li>
  <li>Spoofs the target by pretending to be the gateway</li>
  <li>Spoofs the gateway by pretending to be the target</li>
  <li>Maintains the spoofed connection continuously</li>
  <li>Restores the original ARP tables when interrupted</li>
</ul>

---

<h2>📄 Script Overview</h2>

<ul>
  <li><code>get_user_input()</code> → Handles CLI arguments</li>
  <li><code>get_mac_address()</code> → Retrieves MAC addresses</li>
  <li><code>arp_poisoning()</code> → Sends spoofed ARP responses</li>
  <li><code>arp_resetting()</code> → Restores correct ARP tables</li>
</ul>

---

<h2>📡 Example Output</h2>

<pre>
Sending ARP Poisoning packets ...2
Sending ARP Poisoning packets ...4
Sending ARP Poisoning packets ...6
</pre>

<p>Stop the attack using:</p>

<pre>
CTRL + C
</pre>

<p>The script automatically restores the network afterward.</p>

---

<h2>⚠️ Important Notes</h2>

<ul>
  <li>Enable IP forwarding for full MITM traffic forwarding</li>
  <li>Works only on local networks</li>
  <li>Use only in authorized environments or labs</li>
  <li>Requires Scapy to be installed properly</li>
</ul>

<p>Enable IP forwarding (Linux):</p>

<pre>
echo 1 > /proc/sys/net/ipv4/ip_forward
</pre>

<p>Disable afterward:</p>

<pre>
echo 0 > /proc/sys/net/ipv4/ip_forward
</pre>

---

<h2>🛑 Disclaimer</h2>

<p>
This project is strictly for educational purposes, cybersecurity learning, and authorized penetration testing.<br>
Do not use this tool on networks or systems without explicit permission.
</p>

---

<h2>📬 Contributing</h2>

<p>
Feel free to fork this repository and submit pull requests to improve the Project.
</p>

---

<h2>📜 License</h2>

<p>
This Project is licensed under the MIT License.<br>
@Pro-Mousa<br>
© 2026
</p>

<!-- Footer -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=100&color=0:1F1C2C,100:928DAB&section=footer" alt="footer" />
</p>
