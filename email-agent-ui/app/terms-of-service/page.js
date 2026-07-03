"use client";
import Image from "next/image";
import { redirect, useRouter } from "next/navigation";

export default function TermsOfService() {
  return (
    <main className="min-h-screen bg-gray-950 text-white p-8 max-w-3xl mx-auto">
        <button onClick={() => redirect("/")}>
                <Image className="invert" src="/house-solid-full.svg" alt="Home" width={35} height={35 }  />
                </button>
      <h1 className="text-3xl font-bold mb-2">Terms of Service</h1>
      <p className="text-gray-400 mb-8">Last updated: [7/3/2026]</p>

      <p className="mb-6">
        These Terms of Service (&quot;Terms&quot;) govern your use of Email Agent (&quot;we,&quot;
        &quot;our,&quot; or &quot;the App&quot;). By accessing or using the App, you agree to be bound
        by these Terms. If you do not agree, please do not use the App.
      </p>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">1. Description of Service</h2>
        <p>
          Email Agent is a tool that connects to your Gmail account to help you search, organize, and
          draft replies to your emails using AI-assisted processing. You review and approve all drafts
          before they are sent.
        </p>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">2. Eligibility</h2>
        <p>
          You must be at least 13 years old to use Email Agent. By using the App, you represent that
          you meet this requirement and that you have the legal authority to connect the Google
          account you provide.
        </p>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">3. Google Account Access</h2>
        <p>
          To use Email Agent, you must authorize access to your Gmail account through Google&apos;s
          OAuth process. You are responsible for maintaining the security of your Google account. You
          may revoke Email Agent&apos;s access at any time through your{" "}
          <a
            href="https://myaccount.google.com/permissions"
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-400 hover:underline"
          >
            Google Account Permissions
          </a>{" "}
          settings.
        </p>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">4. Acceptable Use</h2>
        <p>You agree not to use Email Agent to:</p>
        <ul className="list-disc list-inside space-y-2 text-gray-300">
          <li>Violate any applicable law or regulation</li>
          <li>Send spam, unsolicited messages, or fraudulent communications</li>
          <li>Access or attempt to access accounts that are not your own</li>
          <li>Interfere with or disrupt the App&apos;s infrastructure or security</li>
          <li>
            Use the App to generate harassing, abusive, deceptive, or otherwise harmful content
          </li>
        </ul>
        <p>
          We reserve the right to suspend or terminate access for any user who violates these terms.
        </p>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">5. AI-Generated Content</h2>
        <p>
          Email Agent uses AI language models to help search your emails and generate draft replies.
          AI-generated content may be inaccurate, incomplete, or inappropriate in some cases. You are
          solely responsible for reviewing and approving any draft before it is sent, and we are not
          liable for the content of emails you choose to send.
        </p>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">6. No Warranty</h2>
        <p>
          Email Agent is provided &quot;as is&quot; and &quot;as available&quot; without warranties of
          any kind, whether express or implied, including but not limited to warranties of
          merchantability, fitness for a particular purpose, or non-infringement. We do not guarantee
          that the App will be uninterrupted, error-free, or completely secure.
        </p>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">7. Limitation of Liability</h2>
        <p>
          To the fullest extent permitted by law, Email Agent and its creators shall not be liable for
          any indirect, incidental, special, consequential, or punitive damages, or any loss of data,
          revenue, or goodwill, arising from your use of or inability to use the App — including any
          emails sent, missed, or misdirected as a result of using the App.
        </p>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">8. Data and Privacy</h2>
        <p>
          Our collection and use of your information is described in our{" "}
          <a href="/privacy" className="text-blue-400 hover:underline">
            Privacy Policy
          </a>
          . By using Email Agent, you also agree to the terms of that policy.
        </p>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">9. Third-Party Services</h2>
        <p>
          Email Agent relies on third-party services, including Google&apos;s Gmail API and AI
          language model providers (such as Google&apos;s Gemini API), to operate. We are not
          responsible for the availability, performance, or policies of these third-party services.
        </p>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">10. Termination</h2>
        <p>
          We reserve the right to suspend or terminate your access to Email Agent at any time, with or
          without notice, for conduct that we believe violates these Terms or is otherwise harmful to
          other users or the App.
        </p>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">11. Changes to These Terms</h2>
        <p>
          We may update these Terms from time to time. Changes will be posted on this page with an
          updated &quot;Last updated&quot; date. Continued use of the App after changes constitutes
          acceptance of the revised Terms.
        </p>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">12. Governing Law</h2>
        <p>
          These Terms shall be governed by and construed in accordance with the laws of [Your
          State/Country], without regard to its conflict of law provisions.
        </p>
      </section>

      <section className="space-y-3 mb-8">
        <h2 className="text-xl font-semibold">13. Contact Us</h2>
        <p>If you have questions about these Terms, please contact us at:</p>
        <p className="text-gray-300">
          Email: [nickc1904work@gmail.com]
          <br />
          App Name: Email Agent
        </p>
      </section>
    </main>
  );
}