# -*- coding: utf-8 -*-
from behave import when, then, given
from nose.tools import assert_equals
from clients.factories import ClientFactory


@when(u'acesso a página inicial')
def access_homepage(context):
    context.browser.visit(context.base_url)


@when(u'clico em "{text}"')
def click_link_by_text(context, text):
    context.browser.find_link_by_partial_text(text).first.click()


@when(u'preencho o formulário do cliente com as seguintes informações')
def fill_client_form(context):
    data = context.table[0]
    context.browser.fill_form({
        'name': data['NOME'],
        'email': data['EMAIL'],
        'birth_date': data['DT. NASC.'],
    })


@when(u'clico no botão "{text}"')
def click_buttob_by_text(context, text):
    xpath_query = u'//button[text()="{0}"]'.format(text)
    context.browser.find_by_xpath(xpath_query).first.click()


@then(u'verei a mensagem "{text}"')
def see_message(context, text):
    assert context.browser.is_text_present(text)


@then(u'verei a seguinte lista dos clientes')
def see_client_list(context):
    clients = context.table.rows
    table = context.browser.find_by_css('#client-list > tbody > tr')
    for row in table:
        data = clients.pop(0)
        cells = row.find_by_tag('td')
        assert_equals(data[0], cells[0].text)
        assert_equals(data[1], cells[1].text)
        assert_equals(data[2], cells[2].text)
    assert_equals(len(clients), 0)  # certify if was read all data


@given(u'que existem {nr_clients} clientes {active_or_inactive} previamente cadastrado')
def create_clients(context, nr_clients, active_or_inactive):
    is_active = active_or_inactive == 'ativos'
    ClientFactory.create_batch(is_active=is_active, size=int(nr_clients))


@when('pare aqui')
@then('pare aqui')
@given('pare aqui')
def stop(context):
    raise StopIteration
