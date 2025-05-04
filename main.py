from virustotal_check import check_virustotal
from contact_scraper import extract_emails_from_url
from save_excel import save_to_excel
import time

final_data = []

with open("websites.txt", "r") as f:
    websites = [line.strip() for line in f if line.strip()]

for idx, site in enumerate(websites, 1):
    print(f"🔍 [{idx}/{len(websites)}] Scanning: {site}")
    malware = check_virustotal(site)
    contact = extract_emails_from_url(site)
    final_data.append([site, malware, contact])
    time.sleep(15)  # To avoid hitting API rate limits

save_to_excel(final_data)
print("✅ Scan complete! Check 'infected_websites.xlsx'")
