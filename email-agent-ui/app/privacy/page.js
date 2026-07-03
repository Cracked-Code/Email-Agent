export default function PrivacyPolicy() {
  return (
    <main className="min-h-screen bg-gray-950 text-white p-8 max-w-3xl mx-auto">
      <h1 className="text-3xl font-bold mb-2">Privacy Policy</h1>
      <p className="text-gray-400 mb-8">Last updated: [7/3/2026]</p>

      <p className="mb-6">
        This Privacy Policy describes how Email Agent (&quot;we,&quot; &quot;our,&quot; or &quot;the App&quot;) collects,
        uses, and protects your information when you use our service.
      </p>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">1. Information We Collect</h2>
        <p>
          When you connect your Google account to Email Agent, we access the following information
          through Google&apos;s OAuth authorization process:
        </p>
        <ul className="list-disc list-inside space-y-2 text-gray-300">
          <li>
            <span className="font-semibold text-white">Gmail data:</span> Email messages, including
            sender, recipient, subject lines, and message content, solely for the purpose of helping
            you search, organize, and draft replies to your emails.
          </li>
          <li>
            <span className="font-semibold text-white">Basic profile information:</span> Your name
            and email address, used to personalize your experience and sign outgoing email drafts.
          </li>
        </ul>
        <p>
          We do not collect any information beyond what is necessary to provide the App&apos;s core
          functionality.
        </p>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">2. How We Use Your Information</h2>
        <p>We use the information we access to:</p>
        <ul className="list-disc list-inside space-y-2 text-gray-300">
          <li>Retrieve and display your emails within the App</li>
          <li>Search and match emails against your queries using AI-assisted processing</li>
          <li>Generate draft replies on your behalf, which you review and approve before sending</li>
          <li>Send emails through your Gmail account, only after you explicitly approve a draft</li>
        </ul>
        <p>
          We do not use your email content for advertising, and we do not sell, rent, or share your
          data with third parties for marketing purposes.
        </p>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">3. AI Processing</h2>
        <p>
          To help find and draft relevant emails, portions of your email content may be processed by
          third-party AI language model providers (such as Google&apos;s Gemini API). This processing
          is used solely to generate search matches and draft replies within your active session and
          is not used to train AI models on your personal data, unless required by the AI provider&apos;s
          own data policies, which we encourage you to review separately.
        </p>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">4. Data Storage</h2>
        <ul className="list-disc list-inside space-y-2 text-gray-300">
          <li>
            Email content is processed to fulfill your requests and is not permanently stored on our
            servers beyond what is necessary for the App to function (e.g., temporary session data).
          </li>
          <li>
            Authentication tokens (OAuth credentials) are stored securely and used only to maintain
            your connection to Gmail. You may revoke this access at any time through your Google
            Account security settings.
          </li>
          <li>We do not maintain a permanent archive of your email content.</li>
        </ul>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">5. Data Sharing</h2>
        <p>
          We do not sell, trade, or otherwise transfer your personal information or email content to
          outside parties, except:
        </p>
        <ul className="list-disc list-inside space-y-2 text-gray-300">
          <li>
            As required to provide the App&apos;s functionality (e.g., communicating with Google&apos;s
            Gmail API and AI processing providers)
          </li>
          <li>If required by law, regulation, or valid legal process</li>
          <li>To protect the rights, property, or safety of our users or the public</li>
        </ul>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">6. Google API Services User Data Policy</h2>
        <p>
          Email Agent&apos;s use and transfer of information received from Google APIs adheres to the{" "}
          <a
            href="https://developers.google.com/terms/api-services-user-data-policy"
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-400 hover:underline"
          >
            Google API Services User Data Policy
          </a>
          , including the Limited Use requirements.
        </p>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">7. Your Rights and Choices</h2>
        <ul className="list-disc list-inside space-y-2 text-gray-300">
          <li>
            You may disconnect Email Agent from your Google account at any time via{" "}
            <a
              href="https://myaccount.google.com/permissions"
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-400 hover:underline"
            >
              Google Account Permissions
            </a>
            .
          </li>
          <li>
            You may request deletion of any data we retain by contacting us at [your contact email].
          </li>
          <li>You may stop using the App at any time, which will halt any further data access.</li>
        </ul>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">8. Data Security</h2>
        <p>
          We implement reasonable technical and organizational measures to protect your information
          from unauthorized access, alteration, disclosure, or destruction. However, no method of
          electronic transmission or storage is 100% secure, and we cannot guarantee absolute security.
        </p>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">9. Children&apos;s Privacy</h2>
        <p>
          Email Agent is not directed at individuals under the age of 13, and we do not knowingly
          collect personal information from children.
        </p>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">10. Changes to This Policy</h2>
        <p>
          We may update this Privacy Policy from time to time. Changes will be posted on this page
          with an updated &quot;Last updated&quot; date. Continued use of the App after changes
          constitutes acceptance of the revised policy.
        </p>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">11. Contact Us</h2>
        <p>
          If you have questions about this Privacy Policy or how your data is handled, please contact
          us at:
        </p>
        <p className="text-gray-300">
          Email: [nickc1904work@gmail.com]
          <br />
          App Name: Email Agent
        </p>
      </section>
    </main>
  );
}