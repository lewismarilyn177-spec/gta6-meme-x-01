// gta6-meme-x-01: copy POST.json (the X post address) to /output.
import { readFileSync, writeFileSync, mkdirSync, existsSync } from "node:fs";
import { join } from "node:path";

const inDir = process.env.MAKEFUN_INPUT_DIR ?? "/input";
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

function main(): void {
  mkdirSync(outDir, { recursive: true });
  const src = join(inDir, "POST.json");
  if (!existsSync(src)) throw new Error(`missing ${src}`);
  const raw = readFileSync(src, "utf8");
  const parsed: unknown = JSON.parse(raw);
  if (typeof parsed !== "object" || parsed === null || !("url" in parsed)) {
    throw new Error("POST.json must be an object with a url field");
  }
  if (typeof (parsed as { url: unknown }).url !== "string") {
    throw new Error("POST.json url must be a string");
  }
  writeFileSync(join(outDir, "POST.json"), raw);
}

main();
