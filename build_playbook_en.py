# -*- coding: utf-8 -*-
"""
Retail AI Scenario Playbook — English edition
---------------------------------------------
21 scenarios across 9 functional tracks, translated from the original Chinese playbook.

Scrubbing rules applied (real-world identifiers removed):
  - store names      -> Store A/B/C ... (city kept, mall name removed)
  - competitor names -> Brand A/B/C ... (listed-company names removed)
  - API keys/tokens  -> <YOUR_API_KEY>
  - internal paths   -> /workspace/demo/data/
  - internal tools   -> "company wiki" / "team chat"
  - asset filenames  -> generic names
All figures are illustrative sample data, as labelled in the original.
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "playbook.html")

TRACKS = [
    {
        "icon": "◎", "name": "Market Insight", "zh": "市场洞察",
        "scenes": [
            {
                "t": "Fashion Trend Daily",
                "d": "Scrapes runway coverage and distills trends along three axes — silhouette, colour, fabric — then pushes a brief on a schedule.",
                "p": "Fetch the last 7 days of runway coverage from the Big Four fashion weeks (Milan / Paris / New York / London), "
                     "focused on Spring/Summer 2026 womenswear, and build a trend brief:\n"
                     "1. Top 5 silhouettes (with visual reference: A-line / tailoring / deconstructed / oversize / utility)\n"
                     "2. Top 5 colours (with Pantone codes + estimated peak month)\n"
                     "3. Top 3 fabrics (with finishing keywords, e.g. pleating, bonded seams, brushed)\n"
                     "4. Which major houses have already picked up these signals — and where same-price-tier competitors overlap\n"
                     "Output: single-file HTML report with a colour-bar visual and silhouette diagrams.",
                "o": "HTML brief · auto-pushed weekly",
            },
            {
                "t": "Industry Landscape Research",
                "d": "Four dimensions — market size, consumer profile, channel structure, risk — delivered as a report + infographic + deck.",
                "p": "Produce a deep research report on the premium womenswear market:\n"
                     "- Market size / growth / concentration (CR5 / CR10)\n"
                     "- Consumer profile (age / income / city tier / purchase frequency)\n"
                     "- Strategic moves by leading brands over the past 12 months\n"
                     "- Channel structure shift (offline / e-commerce / private domain / content platforms)\n"
                     "- Risk points (downgrading spend, inventory turnover, overseas brands returning)\n"
                     "Output:\n"
                     "- Single-file HTML report (table of contents + charts)\n"
                     "- A one-page A3 executive infographic\n"
                     "- A 30-slide investor deck\n"
                     "Tone: restrained and professional. No filler adjectives — every claim needs a number behind it.",
                "o": "HTML report · A3 infographic · 30-slide deck",
            },
            {
                "t": "Listed-Company Earnings Comparison",
                "d": "Cross-company comparison on revenue, margin, inventory turnover and expense ratio, with an ROI heatmap, refreshed each reporting season.",
                "p": "Run a cross-sectional read on the latest results of 7 listed womenswear companies (Brand A through Brand G):\n"
                     "Comparison dimensions:\n"
                     "- Revenue YoY / net margin / inventory turnover / receivables\n"
                     "- Channel mix shift: direct-retail / franchise / e-commerce\n"
                     "- One industry heatmap scoring ROI / growth / inventory health\n"
                     "- A quarterly tracking sheet (.xlsx) kept as a long-lived asset\n"
                     "Schedule:\n"
                     "- Auto-fetch and notify each reporting season (Apr / Aug / Oct / late Jan)\n"
                     "- Push to my inbox and the strategy team wiki",
                "o": "Comparison HTML · ROI heatmap · quarterly tracker",
            },
        ],
    },
    {
        "icon": "◈", "name": "Social Listening (VOC)", "zh": "社媒聆听 VOC",
        "scenes": [
            {
                "t": "Xiaohongshu / RED Consumer Insight",
                "d": "Pulls the top posts of the last 30 days and surfaces hot terms, recurring products and unmet needs — then chains insights into a trend line.",
                "p": "Collect the top 200 notes from the last 30 days on premium womenswear styling and report:\n"
                     "- The 5 product types appearing most often\n"
                     "- Pain points consumers raise unprompted (e.g. \"looks bulky\", \"loses shape\", \"shrinks after washing\")\n"
                     "- Three product improvement recommendations for us\n"
                     "Output: an action list plus a word-cloud visual.\n"
                     "Tip: add \"compare against last month\" so each month's insight forms a trend line automatically.",
                "o": "Action list · word cloud",
            },
            {
                "t": "Sentiment Analysis",
                "d": "Batches scattered reviews into sentiment distribution, issue clusters and an owner-assigned fix list.",
                "p": "Read review batches across platforms and output:\n"
                     "- Sentiment distribution (positive / neutral / negative) with an overall health verdict\n"
                     "- Issue clusters, ranked by frequency\n"
                     "- A remediation list with a suggested owner per item, ready to hand off",
                "o": "Sentiment breakdown · issue clusters · fix list",
            },
            {
                "t": "Hit-Product Teardown",
                "d": "Searches competitor price, fabric and selling points, then produces a cross-reference table and our points of differentiation.",
                "p": "Find comparable in-season styles from three same-tier competitors (similar silhouette / fabric / price) and build a cross-reference table:\n"
                     "- Price, fabric composition, cut, and high-frequency words in user reviews\n"
                     "- Our top 3 differentiation advantages\n"
                     "- Top 3 design elements worth adopting\n"
                     "Tip: swap in the parameters of the styles we actually have in stock — the output gets much sharper.",
                "o": "Cross-reference table · differentiation summary",
            },
            {
                "t": "Competitor & Reputation Comparison",
                "d": "Two search passes — a reputation baseline, then competitor and controversy angles — producing a scored matrix, risk register and response plan.",
                "p": "Two objectives:\n"
                     "Competitive read — where our brand stands against competitors in word of mouth and what users actually compare.\n"
                     "Reputation monitoring — true sentiment health, positive/negative distribution, and negative risk points, with warnings and a response plan.\n\n"
                     "Search strategy (two passes)\n"
                     "Pass 1: search the brand (including name variants), sort by hottest, exclude official accounts, pure ad copy and image-only posts; "
                     "keep the top 5 notes with genuine discussion (reputation baseline).\n"
                     "Pass 2 (two directions, 2–3 notes each):\n"
                     "  competitive angle — \"brand vs brand\", \"is competitor X worth buying\";\n"
                     "  controversy angle — \"complaints\", \"quality\", \"sizing\", \"colour mismatch\", \"pilling/shrinkage\", \"after-sales\".\n"
                     "Merge with pass 1 and settle on the 10 most information-dense notes.\n\n"
                     "Extraction rules\n"
                     "For each note, pull comments with 5+ likes, prioritising questions, brand comparisons and negative disputes. Tag every comment with:\n"
                     "- category (brand comparison / quality doubt / price-value / fit / colour mismatch / after-sales / recommendation / link request)\n"
                     "- sentiment (positive / neutral / negative)\n"
                     "- competitor names mentioned\n\n"
                     "Analysis output\n"
                     "- Sentiment volume and distribution, plus an overall health verdict\n"
                     "- Competitive matrix scored across reputation, quality, price, design, fit, expertise, after-sales — one-line strength, one-line weakness\n"
                     "- Top 5 user pain points by frequency\n"
                     "- Top 5 positive and top 5 negative keywords, listed separately\n"
                     "- Negative risk register graded P0/P1/P2 by severity and reach, with note links and like counts\n"
                     "- Trend judgement and response plan: PR holding line, service-script fixes, QC improvements, competitive plays, monitoring priorities",
                "o": "Comparison matrix · P0–P2 risk register · response plan",
            },
        ],
    },
    {
        "icon": "◆", "name": "Brand Marketing", "zh": "品牌营销",
        "scenes": [
            {
                "t": "Product Poster Generation",
                "d": "One model shot becomes a full set of channel-ready images. Traditional shoot-plus-design took 1–2 weeks; this runs in minutes.",
                "p": "From a single model reference image, generate the channel image set (main image, detail crops, and platform-specific ratios).\n"
                     "Keep garment geometry and colour faithful to the reference. No watermark, no invented logos.\n"
                     "Output: one image per channel spec, named by channel.",
                "o": "Channel-ready image set",
            },
            {
                "t": "Product Copy",
                "d": "Structured parameters plus a product image produce a mobile detail-page demo and copy, cutting launch copy time sharply.",
                "p": "[Product]\n"
                     "- Brand / product name / price / strikethrough price\n"
                     "- Target customer (e.g. urban professional women 30+)\n"
                     "- Price tier (mid / premium / luxury)\n"
                     "- Fabric composition (write \"per care label\" if unknown)\n"
                     "- Size chart (height/weight range for S/M/L)\n"
                     "[Visual]\n"
                     "- Primary colour / tone (e.g. understated luxury / minimal / youthful)\n"
                     "[Structure — 9 modules top to bottom]\n"
                     "1 brand bar · 2 hero image with season badge · 3 price block with hook line and 3–4 selling-point tags · "
                     "4 four numbered selling points with plain-language explanations · 5 fabric and construction detail · "
                     "6 size table with a fit note · 7 three styling scenarios · 8 care and after-sales · 9 CTA buttons\n"
                     "[Copy rules]\n"
                     "- One-line headline, one-line hook. No adjective stacking.\n"
                     "- Lead each selling point with a short phrase, then explain it in plain words.\n"
                     "- Never invent missing facts — default to neutral phrasing such as \"per care label\".\n"
                     "[Technical]\n"
                     "- 375px mobile container, centred on a light grey backdrop. Leave unfilled fields as visible placeholders.",
                "o": "Mobile detail page HTML · copy deck",
            },
            {
                "t": "Product Detail Page",
                "d": "Turns product images and selling points into a selling-point → usage-scenario → construction chain, so the page has a conversion path.",
                "p": "Arrange the product assets into a conversion path: core selling point → usage scenario → construction detail.\n"
                     "Each section must answer a real objection a buyer raises at that point in the scroll.\n"
                     "Output: a single-file mobile page, plus the raw asset list so the numbers stay auditable.",
                "o": "Conversion-path detail page",
            },
            {
                "t": "Campaign Playbook",
                "d": "Splits a promotion into pre-sale, launch, peak and clearance phases, generating discount tiers and stock allocation with risk flags.",
                "p": "Walk the campaign through pre-sale → launch (opening day) → peak (main day) → clearance. For each phase give the time window, "
                     "core objective, main mechanic and GMV share.\n\n"
                     "Then generate the mechanic configuration per phase:\n"
                     "- Tiered spend thresholds (4 tiers)\n"
                     "- Member pricing (member discount, points multiplier, stack rules)\n"
                     "- Stock locking (pre-sale allocation, safety水位, oversell threshold)\n\n"
                     "Stock and settlement checks — 6 stock-side items (lock, oversell, cross-channel, size breaks, release, deposit allocation) "
                     "and 6 settlement-side items (stacking rules, member-price exclusivity, return allocation, commission, tax, price protection).\n\n"
                     "High-risk configuration points — red / amber / green grading. Each red flag (stacked discounts producing negative margin, "
                     "locked stock not released, pre-sale stock unallocated, price protection) must carry a concrete avoidance action.",
                "o": "Phase-by-phase config sheet · risk register",
            },
            {
                "t": "Live-Stream Post-Mortem",
                "d": "Reads the transcript alongside viewership data to find peak and dead-air segments, then outputs a review and a reusable script library.",
                "p": "Read the live-stream transcript together with concurrent-viewer data.\n"
                     "- Identify high-engagement segments and dead-air segments, with timestamps\n"
                     "- Explain what drove each peak and what caused each drop\n"
                     "- Build a reusable script library from the highest-converting lines\n"
                     "- Grade recommendations: P0 (direct GMV impact) / P1 (acquisition and retention) / P2 (data feedback)\n"
                     "Output: review report, segment table, script library.",
                "o": "Review report · segment table · script library",
            },
            {
                "t": "Live-Commerce Competitive Report",
                "d": "Pulls competitor sell-through and placement data by category through a third-party data API, producing a report usable in pre-sales demos.",
                "p": "Pipeline: data acquisition → processing → report output → asset retention.\n\n"
                     "[Sources]\n"
                     "1. Primary: query a configured third-party live-commerce data API (key: <YOUR_API_KEY>) for real-time platform data.\n"
                     "2. Local: read cached brand JSON files under /workspace/demo/data/.\n"
                     "3. Hard rule: cross-validate both sources and annotate any definitional gap. Mark missing data explicitly as \"to confirm\" — never fill by assumption.\n\n"
                     "[Scope]\n"
                     "Our brand plus two competitors · channel: the short-video commerce platform (live + short video + product cards) · "
                     "30-day window primary, 90-day as trend support.\n\n"
                     "[Dimensions]\n"
                     "1 Category structure — sub-category split, share by value and by units (dual view so price differences don't mislead), SKU count and newness cadence\n"
                     "2 Price bands — distribution across four bands; average, median, main band, high/low; discount rate and basket size; who competes on volume vs price vs positioning\n"
                     "3 Hit products — top 10 by 30-day value and units cross-ranked; hit profile; new hits vs evergreen; whether hits sit in the main price band\n"
                     "4 Competitor profile — audience age and spending power, store matrix, content cadence and creator scale, one-line positioning each\n\n"
                     "[Processing requirements]\n"
                     "Multi-source integration into one master table · unit and window alignment · dedupe, outlier detection, missing-value flagging · "
                     "brand × price band × category cross-tab · computed metrics (share, period growth, average price, hit concentration) · "
                     "charts (comparison bars, band distribution, hit ranking, brand radar).\n\n"
                     "[Output]\n"
                     "1. One single-file HTML report (cover, summary, contents, four dimensions, comparison charts, conclusions)\n"
                     "2. One Excel workbook with the raw detail by brand (multiple sheets)\n"
                     "3. A conclusion-first verbal summary ready for a pre-sales pitch\n\n"
                     "[Quality bar]\n"
                     "Demo data must be traceable. Anything unconfirmed is flagged \"to confirm\". Conclusion first, tables clear, material differences highlighted. "
                     "Explain non-obvious financial or data terms in plain language.",
                "o": "HTML report · Excel workbook · pitch summary",
            },
        ],
    },
    {
        "icon": "▣", "name": "Business Analytics", "zh": "经营分析",
        "scenes": [
            {
                "t": "Multi-Source Table Merge",
                "d": "Definitions rarely match across systems, so it runs a data health check and lists every discrepancy before building one wide table — alignment drops from days to a single conversation.",
                "p": "These tables come from different systems.\n"
                     "First, run a data health check: examine [store name], [date], [category] and [currency unit] across all tables for inconsistent definitions. "
                     "For each, list the inconsistent field, how each table writes it, and the blast radius. Do not merge yet — give me the health report first.\n\n"
                     "Then build a store master-data dictionary using these rules:\n"
                     "1. Store names use the official full name (e.g. \"Deji\" → \"Nanjing Deji\"; \"Marina Bay\" → \"Singapore Marina Bay\")\n"
                     "2. Dates normalised to YYYY-MM-DD\n"
                     "3. The store field is uniformly named [store_name]\n"
                     "Output a store code mapping table (official name / aliases per table / city).\n\n"
                     "Finally, merge the 5 tables into one store-level operating wide table, one row per store:\n"
                     "store / city / monthly sales / units / online GMV / offline GMV / referral redemptions / members / average gross margin. "
                     "Online and offline fields must map to the same store. All amounts in yuan.",
                "o": "Health-check report · master-data dictionary · wide table",
            },
            {
                "t": "Weekly Operating Report",
                "d": "Many tables, mixed definitions — so it states metric definitions and reconciliation logic first, then generates the bi-weekly operating report.",
                "p": "Step 1 — Give me a structural overview only, in clear text. Do not change any data; I'll tell you what to adjust.\n\n"
                     "Step 2 — Generate a bi-weekly operating report as an HTML file:\n"
                     "1. Overview: core metrics (UV, orders, conversion rate, basket size, UV value) and the period definition\n"
                     "2. Week comparison: split the two weeks and compute period-over-period; also use the table's own \"vs same period last week\" field as a second view\n"
                     "3. Module analysis: homepage traffic, page/floor efficiency, channel structure, campaign effect, associate operations — one or two key conclusions each\n"
                     "4. Charts per section (trend line, share pie, comparison bars), each paired with a \"data conclusion\" and an \"action recommendation\"\n"
                     "5. Close with \"bi-weekly summary + next week's focus\"\n"
                     "Visual: clean business style, restrained accent colour.",
                "o": "Bi-weekly HTML report with charts",
            },
        ],
    },
    {
        "icon": "▤", "name": "Supply Chain", "zh": "商品供应链",
        "scenes": [
            {
                "t": "Supplier Screening & Evaluation",
                "d": "Verifies pricing, MOQ and quality/legal risk across 3–5 suppliers, then tiers them into recommended, backup and blacklist.",
                "p": "Screen and run a first pricing round against these criteria:\n"
                     "1. Find 3–5 candidate suppliers (verify entity scale via a company registry)\n"
                     "2. Price comparison (quote / MOQ / payment terms / tax included or not)\n"
                     "3. Quality risk assessment (industry reputation / last 12 months of sentiment / legal disputes)\n"
                     "4. Return a recommended tier, a backup tier and a blacklist\n"
                     "Output: supplier comparison matrix, reasoning, and a ready-to-send inquiry email template.",
                "o": "Comparison matrix · tiering · inquiry template",
            },
        ],
    },
    {
        "icon": "▦", "name": "Offline Retail", "zh": "线下零售",
        "scenes": [
            {
                "t": "Inventory Health Alert",
                "d": "Auto-detects fields, runs ABC classification and days-of-cover, and flags both slow-moving and stock-out risk.",
                "p": "ABC classification — inventory value share = stock × unit price; A = top 70%, B = 70–90%, C = final 10%.\n"
                     "Days of cover — current stock ÷ average daily sales, prefer the last 90 days.\n"
                     "Slow-mover alert — cover above 120 days is flagged slow; stock below safety stock is flagged high stock-out risk.\n"
                     "Multi-dimension rollups — by category, supplier, store and season.\n"
                     "Charts — ABC pie, category distribution, cover histogram, risk scatter, supplier comparison, store health.\n\n"
                     "Input Excel must contain: SKU code, category, item name, current stock, safety stock, unit cost, retail price, "
                     "sales in the last 30 (or 90) days, supplier, store.\n\n"
                     "Output: a complete HTML analysis report — overview, category structure, cover health, stock-out risk, "
                     "supplier performance, store comparison — written in plain language for business owners.",
                "o": "HTML report with six chart families",
            },
            {
                "t": "Store Associate Enablement",
                "d": "One new-season assortment becomes selling-point cards, a styling map, display guidance and live scripts — packaged and sent to stores ready to use.",
                "p": "We have 142 new styles this season. Build training material for franchise store managers:\n"
                     "1. Quick-reference selling-point cards (one per style: image + 3 points + 1 objection handler)\n"
                     "2. A styling map (which pieces pair, which form a complete look)\n"
                     "3. Display guidance (window / feature table / fitting-room zone)\n"
                     "4. Live scripts (5 minutes per style × 30 styles)\n"
                     "Output: an online course link plus a packaged download.",
                "o": "Selling-point cards · styling map · display guide · scripts",
            },
        ],
    },
    {
        "icon": "▧", "name": "HR", "zh": "HR",
        "scenes": [
            {
                "t": "Headcount Management Dashboard",
                "d": "Presents the headcount dashboard and an HRBP workspace with matching downloadable sample data — opens and runs without deployment.",
                "p": "Build a headcount management dashboard plus an HRBP workspace view.\n"
                     "Data definitions must line up exactly with the charts and stay traceable.\n"
                     "Include two-level navigation, case lightboxes and interactive charts. Clean business visual. "
                     "Must open directly with no deployment — suitable as ready-made material for HR digitalisation demos.",
                "o": "Interactive dashboard (single file)",
            },
        ],
    },
    {
        "icon": "▨", "name": "Finance", "zh": "财务",
        "scenes": [
            {
                "t": "Finance全景 Cockpit",
                "d": "Covers data preparation through reporting output, presenting the full finance scenario map — a starting point for finance scenario expansion.",
                "p": "Assemble the finance view end to end: data preparation, metric definition, drill-down cockpit and reporting output.\n"
                     "Metric definitions are set per business line rather than copied from a template.\n"
                     "Deliver both an interactive cockpit and the raw Excel behind it, so every figure is auditable.",
                "o": "Drill-down cockpit + raw Excel",
            },
        ],
    },
    {
        "icon": "▩", "name": "Office Productivity", "zh": "办公提效",
        "scenes": [
            {
                "t": "Deck Generation (HTML → editable PPTX)",
                "d": "One topic sentence or one source document produces an editable .pptx — including HTML-to-corporate-deck conversion that can be revised further.",
                "p": "Output a real .pptx file — not an image, not a web page.\n\n"
                     "Core value: automate the entire deck-building chain — read the material, fix the visual language, decide what to say, "
                     "design how it looks, build it page by page, then check and deliver.\n\n"
                     "Conversion mode: turn HTML pages/slides into an editable corporate-style PPTX. Text fidelity 100% (conversion changes layout, not wording); "
                     "visual fidelity 85–90% (shapes re-drawn). Built-in design tokens, 8 component specs, 10 reference page scripts; "
                     "native charts, tables and KPI cards generated in code; self-check and repair pass included.",
                "o": "Editable .pptx",
            },
        ],
    },
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Retail AI Scenario Playbook — 21 Scenarios · 9 Functional Tracks</title>
<meta name="description" content="A structured playbook of 21 delivered retail AI scenarios across 9 functional tracks, each reproducing the prompt-to-deliverable chain.">
<style>
  :root {
    --navy:#1e3a5f; --navy-soft:#2c5282; --ink:#1f2937; --gray:#6b7280;
    --line:#e2e8f0; --soft:#f7f9fc; --accent:#c8a35a;
  }
  *{{margin:0;padding:0;box-sizing:border-box}}
  body{{font-family:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI","Helvetica Neue",Arial,
        "PingFang SC","Microsoft YaHei",sans-serif;color:var(--ink);line-height:1.6;-webkit-font-smoothing:antialiased}}
  .wrap{{max-width:960px;margin:0 auto;padding:0 28px}}
  header.hero{{background:linear-gradient(135deg,#1e3a5f 0%,#2c5282 100%);color:#fff;padding:54px 0 44px}}
  .hero h1{{font-size:34px;font-weight:700;letter-spacing:-.4px;line-height:1.2}}
  .hero .sub{{margin-top:9px;font-size:16px;color:#c3d3e8}}
  .hero p{{margin-top:18px;max-width:680px;font-size:14.5px;color:#dbe6f2}}
  .hero .stats{{margin-top:22px;display:flex;gap:26px;flex-wrap:wrap}}
  .hero .stat b{{display:block;font-size:26px;font-weight:700;line-height:1.1}}
  .hero .stat span{{font-size:12px;color:#a9c0dc;letter-spacing:.6px;text-transform:uppercase}}
  .back{{display:inline-block;margin-top:20px;font-size:13.5px;color:#c3d3e8;text-decoration:none;border-bottom:1px solid rgba(195,211,232,.4)}}
  .back:hover{{color:#fff}}

  .disclaimer{{margin:26px 0 0;padding:12px 16px;background:#fdf8ec;border-left:3px solid var(--accent);
               font-size:13px;color:#6b5a2f;border-radius:0 4px 4px 0}}

  section.track{{padding:34px 0 0}}
  .track-head{{display:flex;align-items:baseline;gap:10px;padding-bottom:8px;border-bottom:2px solid var(--navy);margin-bottom:16px}}
  .track-head .ic{{color:var(--navy);font-size:15px}}
  .track-head h2{{font-size:15px;font-weight:700;color:var(--navy);letter-spacing:1.4px;text-transform:uppercase}}
  .track-head .n{{margin-left:auto;font-size:12.5px;color:var(--gray)}}

  .scene{{border:1px solid var(--line);border-radius:6px;margin-bottom:12px;overflow:hidden;background:#fff}}
  .scene-h{{padding:14px 18px;display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap}}
  .scene-h h3{{font-size:16px;font-weight:700;color:var(--navy)}}
  .scene-h .o{{font-size:12px;color:var(--gray);white-space:nowrap}}
  .scene .d{{padding:0 18px 12px;font-size:14px;color:#374151}}
  details{{border-top:1px solid var(--line)}}
  details summary{{padding:10px 18px;font-size:13px;font-weight:600;color:var(--navy-soft);cursor:pointer;user-select:none}}
  details summary:hover{{background:var(--soft)}}
  details pre{{margin:0;padding:0 18px 16px;font-size:12.5px;line-height:1.62;color:#334155;
               white-space:pre-wrap;font-family:"SF Mono",Menlo,Consolas,monospace;background:var(--soft)}}

  footer{{margin-top:44px;padding:28px 0 44px;border-top:1px solid var(--line);font-size:13.5px;color:var(--gray)}}
  footer a{{color:var(--navy-soft);text-decoration:none}}
  @media(max-width:640px){.wrap{padding:0 18px}.hero h1{font-size:26px}}
</style>
</head>
<body>

<header class="hero">
  <div class="wrap">
    <h1>Retail AI Scenario Playbook</h1>
    <div class="sub">21 delivered scenarios · 9 functional tracks · prompt → deliverable, end to end</div>
    <p>
      Most AI rollouts stall because every team re-invents the prompt from scratch. This playbook turns 21
      scenarios that were actually delivered into something a colleague can pick up and run: each one records
      the prompt, the output shape, and the reasoning behind the metric definitions.
    </p>
    <div class="stats">
      <div class="stat"><b>21</b><span>Scenarios</span></div>
      <div class="stat"><b>9</b><span>Functional tracks</span></div>
      <div class="stat"><b>~80%</b><span>Less build time</span></div>
    </div>
    <a class="back" href="index.html">← Back to portfolio</a>
  </div>
</header>

<div class="wrap">
  <div class="disclaimer">
    <b>On sourcing:</b> this is a rebuilt reference edition. Store names are generic (Store A, B, C…),
    competitor names are anonymised (Brand A–G), credentials are stripped to placeholders, and all figures are
    illustrative sample data used to demonstrate output structure — exactly as labelled in the original.
    The underlying playbook was built on a former employer's internal platform and is not publicly shareable;
    what is presented here is the structure and method.
  </div>

  __TRACKS__

  <footer>
    Junshu Xin · <a href="mailto:junshuxi@usc.edu">junshuxi@usc.edu</a> ·
    <a href="index.html">Portfolio</a> · <a href="https://github.com/BillyXinjs">GitHub</a>
  </footer>
</div>
</body>
</html>
"""


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def render_tracks(tracks):
    out = []
    for tr in tracks:
        scenes = []
        for s in tr["scenes"]:
            scenes.append(
                '<div class="scene">\n'
                '  <div class="scene-h"><h3>{t}</h3><span class="o">{o}</span></div>\n'
                '  <div class="d">{d}</div>\n'
                '  <details><summary>Show prompt</summary><pre>{p}</pre></details>\n'
                '</div>'.format(t=esc(s["t"]), o=esc(s["o"]), d=esc(s["d"]), p=esc(s["p"]))
            )
        out.append(
            '<section class="track">\n'
            '  <div class="track-head"><span class="ic">{ic}</span><h2>{name}</h2>'
            '<span class="n">{n} scenario{s}</span></div>\n'
            '  {scenes}\n'
            '</section>'.format(
                ic=tr["icon"], name=tr["name"], n=len(tr["scenes"]),
                s="" if len(tr["scenes"]) == 1 else "s",
                scenes="\n  ".join(scenes)
            )
        )
    return "\n".join(out)


def main():
    total = sum(len(t["scenes"]) for t in TRACKS)
    assert total == 21, "场景数应为 21，实际 {}".format(total)
    html = TEMPLATE.replace("__TRACKS__", render_tracks(TRACKS))
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print("生成：", OUT, "| 场景数：", total, "| 条线：", len(TRACKS))


if __name__ == "__main__":
    main()
