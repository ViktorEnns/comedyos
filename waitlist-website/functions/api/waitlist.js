/**
 * Cloudflare Pages Function — POST /api/waitlist
 * Automatically deployed by Cloudflare Pages when placed in /functions/api/waitlist.js
 *
 * Supports dual persistence:
 * 1. Google Sheets / Google Forms Webhook (via env.GOOGLE_SHEET_WEBHOOK_URL)
 * 2. Cloudflare KV Edge Storage (optional, via env.WAITLIST_KV binding)
 */

export async function onRequestPost(context) {
  const { request, env } = context;

  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Content-Type': 'application/json',
  };

  try {
    const body = await request.json();
    const email = (body.email || '').trim().toLowerCase();
    const club = (body.club || 'Independent Circuit').trim();
    const vip = Boolean(body.vip);
    const timestamp = body.timestamp || new Date().toISOString();

    if (!email || !email.includes('@')) {
      return new Response(
        JSON.stringify({ ok: false, error: 'Valid email address is required.' }),
        { status: 400, headers: corsHeaders }
      );
    }

    const record = {
      email,
      club,
      vip: vip ? 'FOUNDING_VIP_6MO' : 'STANDARD_BATCH_01',
      timestamp,
      userAgent: request.headers.get('user-agent') || 'unknown',
      country: request.cf?.country || 'unknown',
    };

    // 1. Save to Cloudflare KV if bound in Cloudflare Pages dashboard
    if (env.WAITLIST_KV) {
      await env.WAITLIST_KV.put(`waitlist:${email}`, JSON.stringify(record));
    }

    // 2. Forward to Google Sheets Apps Script Webhook if configured
    if (env.GOOGLE_SHEET_WEBHOOK_URL) {
      await fetch(env.GOOGLE_SHEET_WEBHOOK_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(record),
      });
    }

    return new Response(
      JSON.stringify({
        ok: true,
        message: 'Spot reserved in Comedy OS Batch 01.',
        record: { email, club, vip: record.vip, timestamp },
      }),
      { status: 200, headers: corsHeaders }
    );
  } catch (err) {
    return new Response(
      JSON.stringify({ ok: false, error: 'Failed to process waitlist signup.', details: err.message }),
      { status: 500, headers: corsHeaders }
    );
  }
}

export async function onRequestOptions() {
  return new Response(null, {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    },
  });
}
