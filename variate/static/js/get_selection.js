function get_default_selection(element_id, option_id){
    m=$(element_id);
    let i;
    for(i=0;i<=m.options.length;i++)
        {
        if(m.options[i].value==option_id)
            {
               m.options[i].selected=true;
               break;
            }
        }
}

function $(id){
     return document.getElementById(id);
}

function delete_entry_confirm(entry_id) {
    if (!confirm("delete confirm？")) {
        window.event.returnValue = false;
    }
    else{
        location.href=("/delete_entry/" + entry_id)
    }
}

function type_input(element_id, value) {
    document.getElementById(element_id).value=value;
}

function get_input_value(element_id) {
    let input_value = document.getElementById(element_id).value;
    return input_value
}

function selected_into_input(select_value, input_element_id) {
    let origin_value = get_input_value(input_element_id)
    if (origin_value.length === 0){
        origin_value = select_value
    }else {
        if(origin_value.search(select_value) === -1){
            origin_value = origin_value+','+select_value
        }else{
            if(origin_value.search(select_value+',') === -1){
                if(origin_value.search(','+select_value) === -1){
                    origin_value = origin_value.replace(select_value, '')
                }else {
                    origin_value = origin_value.replace(','+select_value, '')
                }
            }else {
                origin_value = origin_value.replace(select_value+',', '')
            }
        }
    }
    type_input(input_element_id, origin_value)
}

function getCreatorList(){
    $.ajax({
        url: "/get_all_creators",
        type: "get",
        dataType: "json",
        data: 'data',
        success: function (data) {
            var area = document.getElementById("createBy");
            var optionstring = "";
            if (data.length > 0) {
                for (var i = 0; i < data.length; i++) {
                    optionstring += "<option>" + data[i] + "</option>"; //公共变量赋值
                }
            }

            if (area.options.length==0) {                 //如果下拉框没有数据才进行加载
                $("#createBy").html(optionstring);   //下拉框加载数据
                $('#createBy').selectpicker('refresh');
            }
        },

        error: function (data) {
            alert("查询失败" + data);
        }
    })
}
