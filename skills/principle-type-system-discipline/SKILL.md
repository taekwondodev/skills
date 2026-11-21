---
name: principle-type-system-discipline
description: "Apply when designing types, reviewing signatures, or writing code in a statically typed language."
---

# Type System Discipline

Make the compiler reject mismatched primitives, unproven casts, and unhandled variants. Prefer defining errors and special cases out of existence over proliferating handlers. Applies to any typed language. Invalid states and variant modeling belong to the **model-the-domain** principle skill; parsing external data belongs to the **boundary-discipline** principle skill.

- **Types are constructions, not restrictions.** Build types from the values you want instead of restricting looser types with checks. A non-empty list is a head plus a rest; a valid time range is a start plus a duration. Choose a shape that cannot construct the illegal value and expose the interface callers need.
- **Brand semantic primitives.** If two arguments share a primitive type but mean different things, brand them. `UserId` and `OrderId` should not be interchangeable: use branded intersections in TypeScript or newtypes elsewhere.
- **Don't lie to the type system.** Casts, unsafe coercions, and assertions that bypass the compiler risk runtime crashes. Prove the fact through validation, narrowing, or model refinement, or accept that the cast is a hazard. Trace each `any`, `as`, or `assertNotNull` to the boundary that should prove it.
- **Exhaustive matching is the compiler's job.** Adding an unhandled variant must fail compilation, showing the next agent where to add a case. Use your language's idiom: a `never`-typed binding in TypeScript, an unannotated `match` in Rust, `-Werror=incomplete-patterns` in Haskell, or sealed-class match exhaustiveness in Kotlin.
- **Keep representations private.** Expose only what callers need. Prefer private submodules with explicit parent re-exports over exposing internal structure.
- **Derive types from authoritative schemas.** When a protocol buffer, OpenAPI spec, GraphQL schema, database migration, design-system token file, or another file owns a shape, derive from it instead of duplicating the type. See the **encode-lessons-in-structure** principle skill.
- **Strengthen a type only where partiality appears.** A runtime assertion, null check, or "this should never happen" throw marks the place a type is too weak. Push that check up into the type. Then stop. The type system's job is to track the cases each use site must handle, not to describe the data as precisely as possible. Prefer total functions. `sum` of an empty list is 0, so it takes the plain list. `head` of an empty list has no answer, so it demands the non-empty one. If nothing would otherwise panic, keep the plain type. Extra precision costs reuse and ceremony and buys no safety.