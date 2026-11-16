import asyncio
import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_sms_campaign_delivery_and_failover():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # Mock Telco Gateway Dashboard endpoint
        await page.route("**/api/sms/campaign", lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body='{"campaign_id": "CMP-101", "status": "DELIVRD", "route": "PRIMARY_SMPP"}'
        ))
        
        await page.set_content("""
            <html>
                <body>
                    <button id="trigger-sms">Send Bulk SMS</button>
                    <div id="status">Pending</div>
                    <script>
                        document.getElementById('trigger-sms').onclick = async () => {
                            const res = await fetch('/api/sms/campaign');
                            const data = await res.json();
                            document.getElementById('status').innerText = data.status;
                        };
                    </script>
                </body>
            </html>
        """)
        
        await page.click("#trigger-sms")
        status_text = await page.inner_text("#status")
        assert status_text == "DELIVRD"
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_sms_campaign_delivery_and_failover())
