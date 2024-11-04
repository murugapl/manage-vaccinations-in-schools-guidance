import MarkdownIt from 'markdown-it'
import markdownItAnchor from 'markdown-it-anchor'
import markdownItImageFigures from 'markdown-it-image-figures'
import markdownItMark from 'markdown-it-mark'
import markdownItTableOfContents from 'markdown-it-table-of-contents'
import { figureRules } from './markdown-it/figure.js'

/**
 * Configure markdown-it
 * @see {@link https://markdown-it.github.io/markdown-it/}
 * @param {object} [options] - Plugin options
 * @returns {Function} markdown-it instance
 */
export function md(options = {}) {
  const opts = {
    breaks: true,
    html: true,
    linkify: false,
    typographer: true
  }

  const md = new MarkdownIt(opts)
    .use(markdownItAnchor, {
      permalink: options.headingPermalinks
        ? markdownItAnchor.permalink.headerLink({
            class: 'app-link--heading',
            safariReaderFix: true
          })
        : false
    })
    .use(markdownItImageFigures, {
      async: true,
      classes: 'nhsuk-image__img',
      figcaption: true,
      lazy: true
    })
    .use(markdownItMark)
    .use(markdownItTableOfContents, {
      includeLevel: [2],
      listType: 'ol',
      transformContainerOpen: () => {
        return '<nav class="nhsuk-contents-list"><h2 class="nhsuk-u-visually-hidden">Contents</h2>'
      },
      transformContainerClose: () => {
        return '</nav>'
      }
    })
    .use(figureRules)

  return md
}
