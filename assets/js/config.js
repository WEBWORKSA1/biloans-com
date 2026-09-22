/* BiLoans.com — site configuration. Edit values here; no other code changes needed. */
window.BL_CONFIG = {
  siteName: "BiLoans",
  siteUrl: "https://webworksa1.github.io/biloans-com/", // change to https://biloans.com/ after DNS
  ratesAsOf: "September 2026",

  /* Google AdSense — paste your publisher ID (ca-pub-XXXXXXXXXXXXXXXX) to switch every ad slot live.
     Leave empty to show house ads ("Advertise here") instead. */
  adsenseClient: "",
  adsenseSlots: { header: "", inArticle: "", sidebar: "", footer: "" },

  /* Forms: all submissions go to one inbox through FormSubmit (formsubmit.co).
     After the first submission you receive an activation e-mail; FormSubmit then offers a random
     alias string. Paste it below to remove even the obfuscated address from the code path. */
  formAlias: "",

  /* Donation / payment links (optional). Leave "" to use the pledge form only. */
  payments: {
    paypal: "",        // e.g. https://www.paypal.com/donate/?hosted_button_id=XXXX
    buymeacoffee: "",  // e.g. https://buymeacoffee.com/yourname
    stripe: "",        // e.g. https://buy.stripe.com/XXXX
    kofi: ""
  },

  /* YouTube — your channel URL and video IDs to feature (11-char IDs). Empty IDs show topic cards. */
  youtube: {
    channel: "https://www.youtube.com/results?search_query=personal+loans+explained",
    featured: { id: "", title: "How to compare personal loans in 5 minutes" }
  },

  social: { x: "#", facebook: "#", linkedin: "#", instagram: "#", youtube: "#", tiktok: "#" },

  /* Donation goals shown on /support.html (edit amounts as funds come in) */
  goals: [
    { key: "Operations", raised: 0, target: 3000 },
    { key: "Promotions & Marketing", raised: 0, target: 5000 },
    { key: "Hiring Talent", raised: 0, target: 8000 },
    { key: "Contests & Prizes", raised: 0, target: 2500 }
  ]
};
