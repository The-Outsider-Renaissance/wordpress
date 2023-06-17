(
function ( blocks, editor, element, blockEditor, components ) {
  const el = element.createElement;
  const useState = element.useState;
  const useBlockProps = blockEditor.useBlockProps;

  async function loadUsers(setUserResult) {
    // TODO: Complete API call to ajaxurl + action
  }

  function buildTeamMembers(userData) {
    // TODO: Helper function to build nested elements from Team
  }

  function Team() {
    const _state = useState(null), userResult = _state[0], setUserResult = _state[1];
    // TODO: Build root element
    // Hint: Chain `el` method calls.
    // Mmay look something like: return(el('div', null, buildTeamMembers()))
  }

  function Edit(_a) {
    const blockProps = useBlockProps();
    return el('div', Object.assign({}, blockProps), el(Team, null));
  }

  function Save(_a) {
    console.log('noop');
  }

  blocks.registerBlockType( 'custom-plugin/team', { edit:Edit, save:Save });
}
) (
  window.wp.blocks,
  window.wp.editor,
  window.wp.element,
  window.wp.blockEditor,
  window.wp.components
);
