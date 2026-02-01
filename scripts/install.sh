#!/bin/bash
# Skill installation/uninstallation/update script

set -e

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
SKILLS_DIR="$PROJECT_ROOT/skills"
CLAUDE_SKILLS_DIR="$HOME/.claude/skills"
CLAUDE_PLUGINS_DIR="$HOME/.claude/plugins"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Functions
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

list_skills() {
    print_info "Available skills:"
    echo ""

    if [ ! -d "$SKILLS_DIR" ]; then
        print_warning "No skills directory found."
        return 1
    fi

    local count=0
    for skill_dir in "$SKILLS_DIR"/*/; do
        if [ -d "$skill_dir" ]; then
            skill_name=$(basename "$skill_dir")
            version_file="$skill_dir/VERSION"

            if [ -f "$version_file" ]; then
                version=$(cat "$version_file")
                echo "  • $skill_name (v$version)"
                ((count++))
            fi
        fi
    done

    if [ $count -eq 0 ]; then
        print_warning "No skills found."
    fi

    echo ""
}

install_skill() {
    local skill_name="$1"
    local skill_source="$SKILLS_DIR/$skill_name"
    local skill_dest="$CLAUDE_SKILLS_DIR/$skill_name"

    # Check if skill exists
    if [ ! -d "$skill_source" ]; then
        print_error "Skill '$skill_name' not found in $SKILLS_DIR"
        return 1
    fi

    # Check if skill has SKILL.md
    if [ ! -f "$skill_source/SKILL.md" ]; then
        print_error "Skill '$skill_name' does not have a SKILL.md file"
        return 1
    fi

    print_info "Installing '$skill_name'..."

    # Create destination directory
    mkdir -p "$CLAUDE_SKILLS_DIR"

    # Copy skill directory
    cp -r "$skill_source" "$skill_dest"

    # Make scripts executable
    find "$skill_dest/scripts" -type f -name "*.py" -exec chmod +x {} \; 2>/dev/null || true
    find "$skill_dest/scripts" -type f -name "*.sh" -exec chmod +x {} \; 2>/dev/null || true

    print_success "Installed '$skill_name' to $skill_dest"
}

install_all() {
    print_info "Installing all skills..."

    if [ ! -d "$SKILLS_DIR" ]; then
        print_error "No skills directory found."
        return 1
    fi

    local installed=0
    local failed=0

    for skill_dir in "$SKILLS_DIR"/*/; do
        if [ -d "$skill_dir" ]; then
            skill_name=$(basename "$skill_dir")

            if install_skill "$skill_name"; then
                ((installed++))
            else
                ((failed++))
            fi
        fi
    done

    echo ""
    print_success "Installation complete: $installed installed, $failed failed"
}

uninstall_skill() {
    local skill_name="$1"
    local skill_dest="$CLAUDE_SKILLS_DIR/$skill_name"

    if [ ! -d "$skill_dest" ]; then
        print_warning "Skill '$skill_name' is not installed."
        return 0
    fi

    print_info "Uninstalling '$skill_name'..."
    rm -rf "$skill_dest"
    print_success "Uninstalled '$skill_name'"
}

update_skill() {
    local skill_name="$1"

    print_info "Updating '$skill_name'..."
    uninstall_skill "$skill_name"
    install_skill "$skill_name"
}

update_all() {
    print_info "Updating all installed skills..."

    if [ ! -d "$CLAUDE_SKILLS_DIR" ]; then
        print_warning "No skills directory found in $CLAUDE_SKILLS_DIR"
        return 0
    fi

    local updated=0
    local failed=0

    for skill_dir in "$CLAUDE_SKILLS_DIR"/*/; do
        if [ -d "$skill_dir" ]; then
            skill_name=$(basename "$skill_dir")

            if [ -d "$SKILLS_DIR/$skill_name" ]; then
                if update_skill "$skill_name"; then
                    ((updated++))
                else
                    ((failed++))
                fi
            else
                print_warning "Skipping '$skill_name' - not found in source"
            fi
        fi
    done

    echo ""
    print_success "Update complete: $updated updated, $failed failed"
}

show_help() {
    cat << EOF
Kenpetex Skills Installation Script

Usage: $0 <command> [skill-name]

Commands:
  list           List all available skills
  all            Install all skills
  <skill-name>   Install a specific skill
  uninstall      Uninstall a specific skill
  update         Update a specific skill
  update-all     Update all installed skills
  help           Show this help message

Examples:
  $0 list
  $0 all
  $0 my-skill
  $0 uninstall my-skill
  $0 update my-skill
  $0 update-all

EOF
}

# Main
main() {
    if [ $# -eq 0 ]; then
        show_help
        exit 0
    fi

    case "$1" in
        list)
            list_skills
            ;;
        all)
            install_all
            ;;
        uninstall)
            if [ -z "$2" ]; then
                print_error "Please specify a skill name to uninstall"
                echo "Usage: $0 uninstall <skill-name>"
                exit 1
            fi
            uninstall_skill "$2"
            ;;
        update)
            if [ -z "$2" ]; then
                print_error "Please specify a skill name to update"
                echo "Usage: $0 update <skill-name>"
                exit 1
            fi
            update_skill "$2"
            ;;
        update-all)
            update_all
            ;;
        help|--help|-h)
            show_help
            ;;
        *)
            # Assume it's a skill name to install
            install_skill "$1"
            ;;
    esac
}

main "$@"
