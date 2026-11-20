import { readFileSync, writeFileSync, mkdirSync, existsSync } from "node:fs";
import { join } from "node:path";

const inputDir = process.env.MAKEFUN_INPUT_DIR || "/input";
const outputDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";

const inputPath = join(inputDir, "POST.json");
const outputPath = join(outputDir, "POST.json");

if (!existsSync(inputPath)) {
  throw new Error(`Input file not found: ${inputPath}`);
}

let raw: Buffer;
try {
  raw = readFileSync(inputPath);
} catch (err) {
  throw new Error(`Failed to read ${inputPath}: ${(err as Error).message}`);
}

let parsed: unknown;
try {
  parsed = JSON.parse(raw.toString());
} catch (err) {
  throw new Error(`Invalid JSON in ${inputPath}: ${(err as Error).message}`);
}

if (typeof parsed !== "object" || parsed === null || !("url" in parsed)) {
  throw new Error("POST.json must be an object containing a string field \"url\"");
}

const obj = parsed as Record<string, unknown>;
if (typeof obj.url !== "string") {
  throw new Error("POST.json must be an object containing a string field \"url\"");
}

if (!existsSync(outputDir)) {
  mkdirSync(outputDir, { recursive: true });
}

writeFileSync(outputPath, raw);