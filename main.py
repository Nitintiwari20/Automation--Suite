from file_organizer import organize_files
from web_scraper import scrape_news
from system_monitor import monitor_system
from email_automation import send_email

def run_suite():
    organize_files("C:/Users/YourName/Downloads")
    headlines = scrape_news()
    monitor_system()
    send_email("Daily Automation Report", "\n".join(headlines), "20nitin9tiwari2005@.com")

if __name__ == "__main__":
    run_suite()

