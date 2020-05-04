function get_default_selection(id){
    m=$("edit_catalog");
    for(i=0;i<=m.options.length;i++)
        {
        if(parseInt(m.options[i].value)==parseInt(id))
            {
               m.options[i].selected=true;
               break;
            }
        }
}
function $(id){
     return document.getElementById(id);
}