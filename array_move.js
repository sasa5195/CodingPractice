function move(input, from, to) {
  return input.splice(to, 0, input.splice(from, 1)[0]);
}

const cols = [
  "keyword_bid_update_state",
  "inference_date",
  "keyword_id",
  "brand_code",
  "primary_asin",
  "item_name",
  "portfolio_name",
  "portfolio_id",
  "campaign_name",
  "campaign_id",
  "ad_group_name",
  "ad_group_id",
  "keyword_text",
  "keyword_match_type",
  "keyword_status",
  "roas",
  "roas_targeted_inference",
  "roas_expected_inference",
  "roas_delta",
  "inference_batch_id",
  "total_impressions",
  "total_clicks",
  "total_spend_usd",
  "total_orders",
  "total_sales_usd",
  "ctr",
  "cpc_usd",
  "cvr",
  "acos",
];


console.log(move(cols, 2, 5));