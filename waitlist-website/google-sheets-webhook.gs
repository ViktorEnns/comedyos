/**
 * Google Apps Script — Comedy OS Waitlist Google Sheet Webhook
 *
 * SETUP INSTRUCTIONS (Takes 60 seconds):
 * 1. Create a new Google Sheet (e.g., "Comedy OS Waitlist").
 * 2. In Row 1, add headers: Timestamp | Email | Home Club / City | Tier | Country | User Agent
 * 3. Click Extensions -> Apps Script, paste this code, and click Save.
 * 4. Click "Deploy" -> "New deployment" -> Select type: "Web app".
 * 5. Set "Execute as: Me" and "Who has access: Anyone".
 * 6. Copy the generated Web App URL and add it to Cloudflare Pages environment variables as:
 *    GOOGLE_SHEET_WEBHOOK_URL
 */

function doPost(e) {
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    var payload = JSON.parse(e.postData.contents);

    sheet.appendRow([
      payload.timestamp || new Date().toISOString(),
      payload.email || '',
      payload.club || 'Independent Circuit',
      payload.vip || 'STANDARD_BATCH_01',
      payload.country || 'unknown',
      payload.userAgent || 'unknown'
    ]);

    return ContentService
      .createTextOutput(JSON.stringify({ ok: true }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ ok: false, error: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
