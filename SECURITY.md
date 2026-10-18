# Security policy

## Supported version

Security reports should include the exact toolkit version and affected file or
component. The current release is recorded in `VERSION`.

## Reporting a vulnerability

Please do not publish exploitable details in a public issue. Until a private
security contact is published by the repository owner, contact the maintainer
through GitHub's private vulnerability reporting feature if it is enabled. If
that feature is unavailable, open a minimal public issue asking for a private
reporting channel without posting secrets or exploit details.

## Scope

Relevant reports include unsafe installation or upgrade behavior, path or
symlink handling, unintended file overwrites, credential or private-data
exposure, supply-chain risks, and instructions that encourage unsafe tool use.

## Limitations

The toolkit is not a security boundary and does not sandbox a coding agent. Host
permissions and tool configuration determine what an agent can actually do.
A clean static or skill scan is not proof of safety.
