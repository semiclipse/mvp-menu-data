# Security review — mvp-menu-data

Review date: November 16, 2026  
Reviewed branch: `main`  
Reviewed revision: [`1016f608d2b76d70f476b28a9d82cbf995daa88c`](https://github.com/semiclipse/mvp-menu-data/tree/1016f608d2b76d70f476b28a9d82cbf995daa88c)

This repository-specific extract records the prior static security review; it is not a fresh audit of later commits. Publishing this document changes documentation only. No security fix, dependency update or repository-setting change has been applied.

## Applicable findings

### F6 — Low: mvp-menu-data uses a mutable action tag

**Status:** confirmed supply-chain hardening gap.

[The validation workflow](https://github.com/semiclipse/mvp-menu-data/blob/1016f608d2b76d70f476b28a9d82cbf995daa88c/.github/workflows/validate.yml#L11) uses `actions/checkout@v4` instead of a full immutable commit SHA. A future change or compromise of that tag changes code executed by CI.

The workflow already limits the token to read-only contents and disables persisted credentials, reducing impact. No unsafe pull-request-target pattern or secret exposure was found in this workflow.

**Suggested fix:** pin the action to a reviewed full commit SHA and use an update mechanism to maintain it.

### F5 — Repository safeguard: main reported unprotected

**Observation on November 16, 2026:** GitHub's `/branches/main` endpoint returned `protected: false` for this repository. This is a hardening opportunity, not evidence of a breach.

An unprotected branch does not make a private repository public or allow outsiders to write. It means the endpoint reports no branch protection enforcing safeguards on changes by people or integrations that already have write access. Mistaken direct pushes, force pushes or a compromised write credential can therefore have greater consequences.

**General fix:** in GitHub Settings → Rules → Rulesets, configure an active branch ruleset targeting `main`: require pull requests, require existing relevant CI checks, restrict deletion and block force pushes. For a solo-maintained repository, a pull-request requirement can be used without requiring another person's approval. Keep bypass permissions narrow and deliberate.

Availability depends on the GitHub plan: public repositories can use rulesets on GitHub Free; private repositories generally require Pro, Team or Enterprise. If unavailable under the current plan, use feature branches, deliberate PR reviews and documented merge gates; these are workflow conventions, not automatically enforced protection. No plan upgrade or settings change is authorized by this report. [GitHub documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).

**Limit:** detailed administrative settings, effective rules, bypass lists and account-wide controls were not fully audited. The review connection could not access the attempted detailed branch-protection endpoint. Verify effective settings in GitHub before treating this as a complete policy assessment.

## Coverage and limitations

- 13 selected text files were retrieved and pattern-screened, followed by contextual inspection of security-relevant paths. This was not a line-by-line audit of every file.
- Other branches, full Git history, Git LFS/binary contents, shipped builds and deployment configuration were excluded.
- Account MFA, collaborator permissions, token scopes, cloud-service settings and a full GitHub security-alert inventory were not audited.
- No runtime exploit, application build or regression suite was run. Selected advisory checks are not a complete scan of all transitive dependencies.

Recommendations are informational. Preserve the current intentional playtest behavior unless the owner authorizes a change.
