export default {
  repository: 'https://github.com/ekovegeance/docs',
  titleSuffix: ' – docs',
  logo: (
    <>
      <span className="mr-2 font-extrabold hidden md:inline">ekovegeance</span>
      <span className="text-gray-600 font-normal hidden md:inline">
        Documentation
      </span>
    </>
  ),
  head: (
    <>
      <meta name="msapplication-TileColor" content="#ffffff" />
      <meta name="theme-color" content="#ffffff" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <meta httpEquiv="Content-Language" content="en" />
      <meta name="description" content="Docs - ekovegeance" />
      <meta name="og:description" content="Docs - ekovegeance" />
      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:image" content="https://docs.ekovegeance.com/og.png" />
      <meta name="twitter:site:domain" content="docs.ekovegeance.com" />
      <meta name="twitter:url" content="https://docs.ekovegeance.com" />
      <meta name="og:title" content="Docs - ekovegeance" />
      <meta name="og:image" content="https://docs.ekovegeance.com/og.png" />
      <meta name="apple-mobile-web-app-title" content="Docs" />
      <link
        rel="apple-touch-icon"
        sizes="180x180"
        href="/favicon.png"
      />
      <link
        rel="icon"
        type="image/png"
        sizes="192x192"
        href="/favicon.png"
      />
      <link
        rel="icon"
        type="image/png"
        sizes="32x32"
        href="/favicon.png"
      />
      <link
        rel="icon"
        type="image/png"
        sizes="96x96"
        href="/favicon.png"
      />
      <link
        rel="icon"
        type="image/png"
        sizes="16x16"
        href="/favicon.png"
      />
      <meta name="msapplication-TileImage" content="/ms-icon-144x144.png" />
    </>
  ),
  search: true,
  prevLinks: true,
  nextLinks: true,
  footer: true,
  footerEditOnGitHubLink: false,
  footerText: <>MIT {new Date().getFullYear()} © ekovegeance.</>,
}
