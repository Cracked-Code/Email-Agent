"use client";
import { useState, useEffect } from "react";

export default function Home() {
  const [step, setStep] = useState(1);
  const [account, setAccount] = useState("");
  const [name, setName] = useState("");
  const [emails, setEmails] = useState([]);
  const [loading, setLoading] = useState(false);
  const [query, setQuery] = useState("");
  const [matches, setMatches] = useState([]);
  const [selectedEmail, setSelectedEmail] = useState(null);
  const [draft, setDraft] = useState("");
  const [feedback, setFeedback] = useState("");
  const [authenticated, setAuthenticated] = useState(false);

  function connectGmail() {
    window.location.href = `https://email-agent-api-bvjy.onrender.com/auth/login?account=${account}`;
  }
  async function fetchEmails(accountOverride = null) {
  const accountToUse = accountOverride || account;
  if (accountOverride) setAccount(accountOverride);
  setLoading(true);
  const res = await fetch("https://email-agent-api-bvjy.onrender.com/fetch-emails", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ account: accountToUse, name }),
  });
  const data = await res.json();
  localStorage.setItem("account", accountToUse);
  localStorage.setItem("name", name);
  setEmails(data.emails);
  setLoading(false);
  setStep(2);
}
  async function searchEmails() {
    setLoading(true);
    const res = await fetch("https://email-agent-api-bvjy.onrender.com/search-email", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ emails, query }),
    });
    const data = await res.json();
    setMatches(data.matches);
    setLoading(false);
    setStep(3);
  }
  async function getDraft(feedbackText = null) {
  setLoading(true);
  const res = await fetch("https://email-agent-api-bvjy.onrender.com/draft-reply", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      account,
      name,
      current_email: selectedEmail,
      feedback: feedbackText,
    }),
  });
  const data = await res.json();
  setDraft(data.draft_reply);
  setLoading(false);
}

async function approveEmail() {
  setLoading(true);
  const res = await fetch("https://email-agent-api-bvjy.onrender.com/approve", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      account,
      name,
      current_email: selectedEmail,
      draft_reply: draft,
      approval: true,
      feedback: null,
    }),
  });
  await res.json();
  setLoading(false);
  setStep(5);
}


  useEffect(() => {
  const params = new URLSearchParams(window.location.search);
  const accountParam = params.get("account");
  
  if (accountParam) {
    fetchEmails(accountParam);
  } else {
    const savedAccount = localStorage.getItem("account");
    const savedName = localStorage.getItem("name");
    if (savedAccount) {
      setName(savedName || "");
      fetchEmails(savedAccount);
    }
  }
}, []);
  
  return (
    <main className="min-h-screen bg-gray-950 text-white p-8 max-w-2xl mx-auto">
      <h1 className="text-3xl font-bold mb-8">Email Agent</h1>

        {step === 1 && (
    <div className="space-y-4">
      <h2 className="text-xl font-semibold">Connect your account</h2>
      <input
        className="w-full bg-gray-800 rounded p-3 text-white"
        placeholder="Account name (e.g. nickalot03)"
        value={account}
        onChange={(e) => setAccount(e.target.value)}
      />
      <input
        className="w-full bg-gray-800 rounded p-3 text-white"
        placeholder="Your name (for sign-off)"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <button
        className="bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded font-semibold w-full"
        onClick={connectGmail}
        disabled={loading}
      >
        {loading ? "Connecting..." : "Connect To Gmail"}
      </button>
    </div>
  )}

      {step === 2 && (
  <div className="space-y-4">
    <p className="text-green-400">✓ Fetched {emails.length} emails</p>
    <h2 className="text-xl font-semibold">What email are you looking for?</h2>
    <input
      className="w-full bg-gray-800 rounded p-3 text-white"
      placeholder="e.g. email from Ben about National Grid"
      value={query}
      onChange={(e) => setQuery(e.target.value)}
    />
    <button
      className="bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded font-semibold w-full"
      onClick={searchEmails}
      disabled={loading}
    >
      {loading ? "Searching..." : "Search"}
    </button>
  </div>
  )}
      {step === 3 && (
        <div className="space-y-4">
          <p className="text-green-400">✓ Found {matches.length} matches</p>
          <h2 className="text-xl font-semibold">Pick an email to reply to</h2>
          {matches.map((match) => (
            <button
              key={match.index}
              className="w-full text-left bg-gray-800 hover:bg-gray-700 rounded p-4 border border-gray-700"
              onClick={() => {
                setSelectedEmail(emails[match.index]);
                setStep(4);
              }}
            >
              <p className="font-semibold">{match.subject}</p>
              <p className="text-gray-400 text-sm">{match.sender}</p>
            </button>
          ))}
        </div>
      )}

        {step === 4 && (
    <div className="space-y-4">
      <p className="text-green-400">✓ Selected: {selectedEmail?.subject}</p>
      <h2 className="text-xl font-semibold">Draft Reply</h2>
      {!draft && (
        <button
          className="bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded font-semibold w-full"
          onClick={() => getDraft()}
          disabled={loading}
        >
          {loading ? "Drafting..." : "Generate Draft"}
        </button>
      )}
      {draft && (
        <div className="space-y-4">
          <pre className="bg-gray-800 rounded p-4 whitespace-pre-wrap text-sm">
            {draft}
          </pre>
          <button
            className="bg-green-600 hover:bg-green-700 px-6 py-3 rounded font-semibold w-full"
            onClick={approveEmail}
            disabled={loading}
          >
            {loading ? "Sending..." : "Approve & Send"}
          </button>
          <input
            className="w-full bg-gray-800 rounded p-3 text-white"
            placeholder="Not happy? Give feedback and redraft..."
            value={feedback}
            onChange={(e) => setFeedback(e.target.value)}
          />
          <button
            className="bg-yellow-600 hover:bg-yellow-700 px-6 py-3 rounded font-semibold w-full"
            onClick={() => {
              getDraft(feedback);
              setFeedback("");
            }}
            disabled={loading || !feedback}
          >
            Redraft with Feedback
          </button>
        </div>
      )}
    </div>
  )}

  {step === 5 && (
    <div className="space-y-4 text-center">
      <p className="text-4xl">✓</p>
      <h2 className="text-xl font-semibold text-green-400">Email Sent!</h2>
          <button
      className="bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded font-semibold"
      onClick={() => {
        setDraft("");
        setFeedback("");
        setSelectedEmail(null);
        setMatches([]);
        setQuery("");
        fetchEmails(localStorage.getItem("account"));
      }}
    >
      Start Over
    </button>
    </div>
  )}
    </main>
  );
}