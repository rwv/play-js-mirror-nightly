# play-js-mirror-nightly
A nightly mirror of jpd002/Play- JavaScript Version

## Pinned official browser build

This repository includes the official browser assets fetched on 2026-11-07.
Both files reported `Last-Modified: Mon, 26 Oct 2026 15:24:31 GMT`.
The package version identifies that build date; it is not an upstream release tag.
The official endpoint does not expose the source commit for these binaries.

| File | Official source | SHA-256 |
| --- | --- | --- |
| `dist/Play.js` | <https://playjs.purei.org/Play.js> | `5599ff16ae5e3534f9b779736aedfa20661821d57be7f03e587e31ef8d090317` |
| `dist/Play.wasm` | <https://playjs.purei.org/Play.wasm> | `fb6788e6baa1a7e7af90cb2b8395d91d34d0f2d38d1887610c45fc6e2b149edd` |

The JS and WASM are unmodified upstream bytes. `dist/sri.json` records their
SHA-256 Subresource Integrity values. The upstream BSD-2-Clause license is
included as `License.txt`, copied from
[`jpd002/Play-@1f272327`](https://github.com/jpd002/Play-/blob/1f27232772e484bfb79364b751b84f41f4c87481/License.txt).

This Emscripten build uses `Play.js` itself as a module worker; it does not need
`Play.worker.js`. Set `mainScriptUrlOrBlob` to the entry script URL when creating
the module, and use a cross-origin-isolated document for shared WASM memory.

To install an immutable snapshot without depending on npm publication, use
`pnpm add play-js-mirror-nightly@https://codeload.github.com/rwv/play-js-mirror-nightly/tar.gz/<commit-sha>`.

The scheduled npm mirror is currently disabled for inactivity; this snapshot
does not re-enable publication or change its workflow.
