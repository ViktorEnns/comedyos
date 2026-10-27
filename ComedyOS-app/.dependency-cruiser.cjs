/** @type {import('dependency-cruiser').IConfiguration} */
module.exports = {
  forbidden: [
    {
      name: 'no-circular',
      severity: 'error',
      comment: 'Circular dependencies cause state sync loops and initialization bugs.',
      from: {},
      to: { circular: true }
    },
    {
      name: 'ui-must-not-touch-raw-engines',
      severity: 'error',
      comment: 'UI components must go through state/service hooks, never directly into raw OCR or Audio engines.',
      from: { path: '^src/components/' },
      to: { path: '^src/(engines|workers)/' }
    }
  ],
  options: {
    doNotFollow: { path: 'node_modules' },
    tsPreCompilationDeps: true,
    tsConfig: { fileName: 'tsconfig.json' },
    reporterOptions: {
      mermaid: {
        minify: false
      }
    }
  }
};
