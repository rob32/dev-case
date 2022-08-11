const esbuild = require("esbuild");

const isDevServer = process.argv.includes("--dev");

esbuild
  .build({
    entryPoints: ["frontend/css/style.css", "frontend/js/main.js"],
    outdir: "static",
    bundle: true,
    globalName: "main",
    minify: !isDevServer,
    watch: isDevServer && {
      onRebuild(error, result) {
        if (error) console.error("esbuild: watch-build failed:", error);
        else console.log("esbuild: watch-build succeeded:", result);
      },
    },
    loader: {
      ".png": "file",
      ".jpg": "file",
      ".svg": "file",
      ".ttf": "file",
      ".woff": "file",
      ".woff2": "file",
      ".eot": "file",
    },
  })
  .then(() => console.log("Build complete. Check: http://127.0.0.1:8000/ "))
  .catch(() => process.exit(1));
