import { execSync } from 'node:child_process';
import { writeFileSync, mkdirSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const APP_ROOT = resolve(__dirname, '..');
const PROJECT_ROOT = resolve(APP_ROOT, '..');

const TARGET_OUTPUTS = [
  resolve(PROJECT_ROOT, 'docs-site/docs/architecture/DEPENDENCY_GRAPH.md'),
  resolve(PROJECT_ROOT, 'Comedy_OS_Note_Taker_Vault/Architecture/DEPENDENCY_GRAPH.md')
];

try {
  // Generate raw Mermaid syntax from src/
  const mermaidGraph = execSync(
    'npx.cmd depcruise src --include-only "^src" --config .dependency-cruiser.cjs --output-type mermaid',
    { cwd: APP_ROOT, encoding: 'utf-8', shell: true }
  );

  // Run rule audit to check for architectural violations
  let auditStatus = '✅ **Status:** Zero boundary violations or circular dependencies detected.';
  try {
    execSync('npx.cmd depcruise src --config .dependency-cruiser.cjs --output-type err', {
      cwd: APP_ROOT,
      stdio: 'pipe',
      shell: true
    });
  } catch (err) {
    const errorOutput = err.stdout?.toString() || err.message;
    auditStatus = `🚨 **ARCHITECTURAL VIOLATION DETECTED:**\n\`\`\`text\n${errorOutput}\n\`\`\``;
  }

  const markdown = `---
title: Automated Dependency Graph
sidebar_position: 1
icon: "🕸️"
---

# 🕸️ Comedy OS — Live Codebase Dependency Map
*Auto-generated on ${new Date().toISOString().split('T')[0]} via \`npm run map\`*

${auditStatus}

## Module Import Graph
\`\`\`mermaid
${mermaidGraph.trim()}
\`\`\`
`;

  for (const outputPath of TARGET_OUTPUTS) {
    mkdirSync(dirname(outputPath), { recursive: true });
    writeFileSync(outputPath, markdown, 'utf-8');
    console.log(`✔ Synchronized architecture map to: ${outputPath}`);
  }
} catch (error) {
  console.error('Failed to generate dependency map:', error.message);
  process.exit(1);
}
